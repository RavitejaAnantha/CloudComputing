import csv
import json


# data={"synopsis": '\n            This sequel to the smash-hit comic-book epic The Avengers finds the iconic superhero team dealing with a threat of their own making: a sentient robot called Ultron (voice of James Spader), who was originally designed as part of a peacekeeping program. Since the events of the last film, Captain America (Chris Evans), Iron Man (Robert Downey Jr.), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), Hawkeye (Jeremy Renner), and Black Widow (Scarlett Johansson) have been working to take down various cells of a secret society of villains known as HYDRA. Their zeal to make the world a better, safer place inspires Tony Stark, genius billionaire and alter ego of Iron Man, to create Ultron in order to respond to additional threats that the Avengers aren\'t able to handle. Ultron, unfortunately, takes this directive way too seriously -- he believes that world peace can only be achieved by exterminating humanity, and he\'ll stop at nothing to accomplish this goal. The battle between the Avengers and Ultron is further complicated by the appearance of superpowered siblings Quicksilver (Aaron Taylor-Johnson) and Scarlet Witch (Elizabeth Olsen), who ally themselves with the homicidal android. Samuel L. Jackson and Cobie Smulders co-star as, respectively, S.H.I.E.L.D. operatives Nick Fury and Maria Hill. Joss Whedon, writer and director of the previous Avengers movie, returns in both capacities here.        ',
#   "keywords":[ 'aircraft-carrier',' billionaire',' soldier',' Superhero',' team' ],
#   "themes": [ 'Heroic Mission','abc' ],
#   "moods": [ 'Adrenaline Rush','xyz' ]}


def convert():
    with open('genres.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
        writer.writerow(('synopsis', 'genres'))

    with open('themes.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
        writer.writerow(('synopsis', 'themes'))

    with open('moods.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
        writer.writerow(('synopsis', 'moods'))

    with open('data.json', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = json.loads(line)
            if data['synopsis'] != '':
                with open('themes.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
                    for i in range(0, len(data['themes'])):
                        writer.writerow((data['synopsis'].strip(), data['themes'][i]))

                with open('moods.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
                    for i in range(0, len(data['moods'])):
                        writer.writerow((data['synopsis'].strip(), data['moods'][i]))

                with open('genres.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
                    for i in range(0, len(data['genres'])):
                        writer.writerow((data['synopsis'].strip(), data['genres'][i]))
