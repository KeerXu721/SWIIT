import csv
import os


def csv_to_txt(directory: str, input_csv: str):
    """
    Convert contents of a given csv file to txt files.

    :param directory: a directory containing a csv file with data per emoji type
    :param input_csv: a csv file containing tweet data to be converted
    """
    with open(os.path.join(directory, input_csv), newline='', encoding="utf-8") as csvfile:

        # get directory name
        new_dir = os.path.join(directory, input_csv[:-4])

        # create new directory to hold txt files per emoji if it does not already exist
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)

        # read csv file
        reader = csv.DictReader(csvfile)
        for row in reader:
            tweet_id = row['ID']
            comment = row['Comments']

            # get txt file name which corresponds to the data id
            file_name = os.path.join(new_dir, str(tweet_id)+'.txt')

            # write tweet in the txt file
            with open(file_name, 'w', encoding="utf-8") as output:
                output.write(comment)


directory_name = 'data'
for file in os.listdir(directory_name):
    csv_to_txt(directory_name, file)
