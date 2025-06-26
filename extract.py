import json

if __name__ == '__main__':
    # open JSON file in read mode
    with open('data/class_data.json', 'r') as file:
        # load data
        data = json.load(file)

        # get course name, replace spaces with dashes to use in file name
        name = data['name'].replace(' ', '-')

        # extract title and post content
        for post in data['posts']:
            # check for announcements
            if 'announcement' in post:
                # get the creator info
                creator = post['creator']['name']['fullName'].replace(' ', '-')

                # set the name of the file to the publication date, utf-8 encoded text
                # 16 is used to slice the date format
                with open('out/' + name + '_' + creator + '_' + post['publicationTime'][:16] + '.txt', 'w') as output:
                    output.write(post['announcement']['text'])

            # check for course work
            if 'courseWork' in post:
                # use course and assignment title as file name
                assignment = post['courseWork']['title'].replace(' ', '-')
                with open('out/' + name + '_' + assignment, 'w') as output: 
                    output.write(post['courseWork']['description'])