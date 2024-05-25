import os
import random as rand
import shutil

rand.seed(0)


def batching(directory: str, emoji: str):
    """
    Randomly select 5000 files from the dataset and create batches of 100.

    :param directory: a directory containing txt and ann files per emoji type
    :param emoji: the name of the emoji
    """
    # create new directory to hold batches per emoji it does not already exist
    dir_name = os.path.join(os.path.join(os.path.pardir, "swit_files", emoji))
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # keep track of batch count
    batch_idx = 0

    # retrieve text files from the original directory and randomly select 5000 files
    files = os.listdir(os.path.join(os.path.pardir, "processed_data", emoji_name))
    text_files = [file for file in files if file[-4:] == ".txt"]
    random_files = rand.sample(text_files, 5000)

    # put 100 files in each batch
    for i in range(len(random_files)):
        if i % 100 == 0:
            batch_idx += 1
            batch_dir = os.path.join(dir_name, "batch" + str(batch_idx))
            if not os.path.exists(batch_dir):
                os.mkdir(os.path.join(batch_dir))

        # original files
        prev_txt = os.path.join(directory, random_files[i])
        prev_ann = os.path.join(directory, random_files[i][:-4] + ".ann")

        # new files
        new_dir = os.path.join(dir_name, "batch" + str(batch_idx))
        new_txt = os.path.join(new_dir, random_files[i])
        new_ann = os.path.join(new_dir, random_files[i][:-4] + ".ann")

        # copy files from original directory to new directory
        shutil.copyfile(prev_txt, new_txt)
        shutil.copyfile(prev_ann, new_ann)


emoji_names = ["FHBT", "LCF", "SFWT"]
for emoji_name in emoji_names:
    directory_name = os.path.join(os.path.pardir, "processed_data", emoji_name)
    batching(directory_name, emoji_name)
