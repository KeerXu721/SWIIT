import csv
import os
from collections import defaultdict


def csv_to_ann(directory: str, input_csv: str):
    """
    Convert contents of csv file to ann files.

    :param directory: a directory containing a csv file with data per emoji type
    :param input_csv: a csv file containing emoji spans
    """
    with open(os.path.join(directory, input_csv), newline='', encoding="utf-8") as csvfile:

        # create new directory to hold ann file directories if it does not already exist
        if not os.path.exists("ann_files"):
            os.mkdir("ann_files")

        # get directory name
        new_dir = os.path.join("ann_files", input_csv[:-4])

        # create new directory to hold ann files per emoji if it does not already exist
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)

        # keep count of files that have already been seen for tag number
        completed = defaultdict(int)

        # read csv file
        reader = csv.DictReader(csvfile, fieldnames=['id', 'span', 'text'])
        for row in reader:
            tweet_id = row['id']
            span = row['span']
            text = row['text']

            # convert span to tuple
            span_tuple = eval(span)

            # get name of the ann file
            file_name = os.path.join("ann_files", input_csv[:-4], str(tweet_id)+".ann")

            # write emoji span information in the txt file
            with open(file_name, 'a', encoding="utf-8") as output:
                completed[tweet_id] += 1
                tag_num = "T" + str(completed[tweet_id])

                if completed[tweet_id] == 1:
                    output.write(f"{tag_num}\tEmoji {span_tuple[0]} {span_tuple[1]}\t{text}")
                else:
                    output.write(f"\n{tag_num}\tEmoji {span_tuple[0]} {span_tuple[1]}\t{text}")


directory_name = "spans"
for file in os.listdir(directory_name):
    csv_to_ann(directory_name, file)
