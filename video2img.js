var ffmpeg = require('fluent-ffmpeg');

var first_minute = "00:5.000, 00:10.000, 00:15.000, 00:20.000, 00:25.000, 00:30.000, 00:35.000, 00:40.000, 00:45.000, 00:50.000, 00:55.000, 01:00.000"
var second_minute = "01:5.000, 01:10.000, 01:15.000, 01:20.000, 01:25.000, 01:30.000, 01:35.000, 01:40.000, 01:45.000, 01:50.000, 01:55.000, 02:00.000"
var third_minute = "02:5.000, 02:10.000, 02:15.000, 02:20.000, 02:25.000, 02:30.000, 02:35.000, 02:40.000, 02:45.000, 02:50.000, 02:55.000, 03:00.000"
var fourth_minute = "03:5.000, 03:10.000, 03:15.000, 03:20.000, 03:25.000, 03:30.000, 03:35.000, 03:40.000, 03:45.000, 03:50.000, 03:55.000, 04:00.000"
// var fifth_minute = "04:5.000, 04:10.000, 04:15.000, 04:20.000, 04:25.000, 04:30.000, 04:35.000, 04:40.000, 04:45.000, 04:50.000, 04:55.000, 05:00.000"
var timestamps_str = first_minute + ", " + second_minute + ", " + third_minute + ", " + fourth_minute;
var movie_key = process.argv[3];
console.log(process.argv[2]);
ffmpeg(process.argv[2]) //input file here!!!!!!!!!!!
  .noAudio()
  .on('filenames', function(filenames) {
    console.log('Will generate ' + filenames.join(', '))
  })
  .on('error', function(err) { //extra
    console.log('An error occurred: ' + err.message);
  })  
  .on('end', function() {
    console.log('Screenshots taken');
    return 1;
  })
  .screenshots({
    // Will take screens at 20%, 40%, 60% and 80% of the video
    // count: 4, //count ignored if timestamps array used
    //timestamps: ['00:2.000', '00:4.000', '00:6.000', '00:8.000', '00:10.000', '10:00.000'],
    // timestamps: [30.5, '50%', '01:10.123'],
    timestamps: timestamps_str.split(','),
    folder: './output/',
    filename: movie_key + '-thumbnail-at-%s-seconds.jpeg',
    size: '50%'
  });