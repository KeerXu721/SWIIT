import csv
import regex as re
import os


def find_span(directory: str, input_txt: str):
    """
    Find emoji spans in given a txt file.

    :param directory: a directory containing a csv file with data per emoji type
    :param input_txt: a txt file containing a tweet
    """
    # create new directory to hold csv files containing emoji spans if it does not already exist
    if not os.path.exists("spans"):
        os.mkdir("spans")

    # get name of the csv file
    file_name = os.path.join("spans", os.path.basename(directory) + '.csv')

    # open csv file in append mode
    with open(file_name, 'a', newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['file', 'span', 'text'])

        with open(os.path.join(directory, input_txt), newline='', encoding="utf-8") as f:

            # find emoji spans
            pattern = re.compile(r"🥹+|🥲+|😭+")
            matches = pattern.finditer(f.read())

            # write emoji span information in csv file
            for match in matches:
                writer.writerow({'file': input_txt[:-4], 'span': match.span(), 'text': match.group()})


emoji_names = ["FHBT", "LCF", "SFWT"]
for emoji_name in emoji_names:
    directory_name = os.path.join("data", emoji_name)
    for file in os.listdir(directory_name):
        find_span(directory_name, file)
