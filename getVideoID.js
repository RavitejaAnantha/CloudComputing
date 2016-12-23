var YouTube = require('youtube-node');
var elasticsearch = require('elasticsearch');
var youTube = new YouTube();
youTube.setKey('AIzaSyAS_5AJJuKcGnlz9EnKM8QEdoGCgTyobwg');

var fs = require('fs');
var youtubedl = require('youtube-dl'); //download helper pkg
var async = require('async');
//Search on ES: For each movie do this
var bulk_size = 1;
var client = new elasticsearch.Client({
		  host: 'http://search-movies-5zcbuwmhuftqplir3dnm72jd4a.us-east-1.es.amazonaws.com/'
		});


function es_search(){
    var client = new elasticsearch.Client({
        host: 'http://search-movies-5zcbuwmhuftqplir3dnm72jd4a.us-east-1.es.amazonaws.com/'
    });
    client.search({
        index: 'complete_movies',
        // q: '*:*',
        body: {
            size: bulk_size,
            // query: {
            //     match: {
            //         'urls': {
            //             query: 'karthik'
            //         }
            //     }
            // },
            query: {
                bool: {
                    must_not: {
                        exists: {
                            field: "video_urls"
                        }
                    }
                }
            }
        },
        // size: bulk_size
    }).then(function (response) {
        movies=response.hits.hits;
        for (var i = 0; i < movies.length; i++) {
            var no_movies_returned=movies.length;
            var movie=movies[i]._source;
            var id=movies[i]._id
            var title=movie['title']
            var key=movie['key']
            parseYTVideo(title, key,id,no_movies_returned);
            // get_youtube_movie(title,key);
        }
        //series??
        // async.forEach(movies, parseYTVideo, (err, results) => {
        // 	console.log('completely done');
        // 	console.log(err, results);
        // });

    }, function (error) {
        console.trace(error.message);
    });
}
es_search();


function get_youtube_movie(title,key,id, cb){
youTube.search(title+' Trailer', 2, function(error, result) {
	if (error) {
		console.log(error);
	}
	else {
    	if(result.items[0].id.videoId.length > 0){
    		var url = 'http://www.youtube.com/watch?v=' + result.items[0].id.videoId;
    		var video = youtubedl(url);
			video.on('info', function(info) {
	  			console.log('Download started');
	  			console.log('filename: ' + info.filename);
	  			console.log('size: ' + info.size);
			});

			// Will be called if download was already completed and there is nothing more to download.
			video.on('complete', function complete(info) {
				console.log(info);
				console.log('filename: ' + info._filename + ' already downloaded.');
			});

			// video.on('end', function() {
			// 	console.log('finished downloading! upload video to S3!!!');
			// 	cb(null, true);
			// });
			video.on('end', function() {
				console.log('finished downloading! upload video to S3!!!');

				var video = fs.readFileSync('./output/'+key+'.mp4');
				var AWS=require('aws-sdk');
				// var credentials = new AWS.SharedIniFileCredentials({profile: 'default'});
				// AWS.config.credentials = credentials;

				var s3 = new AWS.S3({
				  apiVersion: '2006-03-01',
				  params: {Bucket: 'bigdatagsa277'} //move to config
				});

				s3.upload({
				  Key: key,
				  Body: video,
				  ACL: 'public-read'
				}, function(err, data) {
				  if (err) {
				    console.log('There was an error uploading your video: ', err.message);
				  }
				  console.log('Successfully uploaded video.');
					var url_obj={
                        "youtube_url":url,
                        "s3_url":data['Location']+'?versionId='+data['VersionId']
                    }
                    client.update({
                        index: 'complete_movies',
                        type: 'movie',
                        id: id,
                        body: {
                            // put the partial document under the `doc` key
                            doc: {
                                video_urls:url_obj
                            }
                        }
                    }, function (error, response) {
                        console.log('error is:'+error);
                        console.log('response is'+JSON.stringify(response));
                        fs.unlinkSync('./output/'+key+'.mp4');//Delete file after updating the es
                        cb(null, true);
                    })

				});
			});

			video.pipe(fs.createWriteStream('./output/'+key+'.mp4'));
	  	} else {
	  		console.log('ERROR: No Video ID found');
	  	}
	}
});
}

var video_count = 1;
var parseYTVideo = (title, key,id,no_movies_returned) => {
    async.parallel({
            youtube: (cb) => {
            get_youtube_movie(title,key,id, cb);
}
}, (err, results) => {
        //both Async functions executed
        console.log('movie finished', video_count);
        video_count+=1;
        if (video_count > no_movies_returned){
            console.log('everything finished');
            video_count = 1;
            setTimeout(es_search, 1000);
        }
        if (!err && results) {
            console.log(results);
        } else {
            //iN CASE OMDB errd
            console.log(' err - ', err)
        }
    })
}
