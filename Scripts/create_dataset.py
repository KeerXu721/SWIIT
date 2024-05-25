import csv
import os
import regex as re
import html


def create_dataset(directory: str, input_csv: str):
    """
    Create a preprocessed dataset from a given csv file.

    :param directory: a directory containing a csv file with data per emoji type
    :param input_csv: a csv file containing the original dataset from Kaggle
    """
    emojis = {"face_holding_back_tears": "FHBT", "loudly_crying_face": "LCF", "smiling_face_with_tear": "SFWT"}

    # get name of the csv file to save preprocessed data to
    file_name = os.path.join(os.path.pardir, "processed_data", emojis[input_csv[:-4]] + '.csv')

    # open csv file in append mode
    with (open(file_name, 'a', newline='', encoding="utf-8") as csvfile):
        writer = csv.DictWriter(csvfile, fieldnames=['ID', 'Comments'])
        writer.writeheader()
        idx = 1  # unique index for each tweet

        with open(os.path.join(directory, input_csv), newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # regex pattern for strings without any of the three emojis
            no_emoji = r"^[^🥹😭🥲]+$"

            # regex pattern for strings where the three emojis are always accompanied by at least another character
            not_only_emoji = r"[🥹😭🥲]+[^🥹😭🥲]+|[^🥹😭🥲]+[🥹😭🥲]+"

            for row in reader:
                text = html.unescape(row['Text'])
                if not re.search(no_emoji, text):
                    removed_user = re.sub(r"@[\S]+[\s]*", "", text)  # remove usernames from the text
                    text = re.sub(r"[\s]*https[\S]+", "", removed_user)  # remove URLs from the text
                if re.search(not_only_emoji, text):
                    text.strip()  # remove leading and trailing whitespace
                    writer.writerow({'ID': idx, 'Comments': text})
                    idx += 1


directory_name = os.path.join(os.path.pardir, "original_data")
for file in os.listdir(directory_name):
    create_dataset(directory_name, file)
