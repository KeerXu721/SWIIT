import csv
import os


def txt_to_csv(directory: str, annotator: str):
    """
    Create a csv file compiling the data from the txt files in the given directory.

    :param directory: a directory containing directories of txt files
    :param annotator: the name of the annotator
    """
    emoji_names = ["FHBT", "LCF", "SFWT"]
    for emoji in emoji_names:
        # get name of the csv file
        file_name = os.path.join(directory, annotator, emoji + '-tweets.csv')

        main_dir = os.path.join(directory, annotator, emoji)

        # open csv file in append mode
        with open(file_name, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'text'])
            writer.writeheader()

            for file in os.listdir(main_dir):
                with open(os.path.join(main_dir, file), newline='', encoding="utf-8") as f:
                    # keep track of the tweet id
                    idx = os.path.basename(file).rsplit(".")[0]

                    # only read data from .txt files
                    if f.name[-3:] == "txt":
                        text = f.read()
                        writer.writerow({'id': idx, 'text': text})


directory_name = os.path.join(os.path.pardir, "annotated_data", "external")
for annotator_name in os.listdir(os.path.join(directory_name)):
    txt_to_csv(directory_name, annotator_name)
