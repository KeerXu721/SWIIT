import csv
import os
from collections import Counter

import emoji


def process_emoji(input_file: str, output_file: str, emoji_name: str):
    with open(input_file, 'r', encoding='utf-8') as f:
        with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
            csv_writer = csv.writer(out_file)
            csv_writer.writerow(['ID', 'Comments'])
            csv_reader = csv.reader(f)
            id = 0
            # dictionary to store every comment, key is the id
            # value is a tuple that contains comments and the pure
            comment_dict = {}
            dominate_emoji = ':' + emoji_name + ':'
            # dominate_emoji_character = emoji.emojize(dominate_emoji)
            for item in csv_reader:
                if len(item) == 0:
                    continue
                item = item[0]
                item_l = item.split(" ")
                comment = ' '.join([i for i in item_l if "@" not in i and 'https' not in i])
                character_counter = Counter(comment)
                emojis = {}
                for char, count in character_counter.items():
                    if emoji.is_emoji(char):
                        emojis.update({char: count})
                if len(emojis) == 1 and emoji.demojize(list(emojis.keys())[0]) == dominate_emoji:
                    id += 1
                    csv_writer.writerow([id, comment])


directory = 'Data/archive'
for filename in os.listdir(directory):
    emoji_name = filename.replace('.csv', '')
    print(emoji_name)
    process_emoji("Data/archive/"+filename, "Data/processed_data/"+filename, emoji_name)

# process_emoji("archive/smiling_face.csv", 'processed_data/smiling_face.csv', 'smiling_face_with_smiling_eyes')
