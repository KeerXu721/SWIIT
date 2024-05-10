# SWiT: Emoji Annotation Scripts

**Author:** Kasey La

This folder contains 8 files:

1. This **README** file.
2. **ann_to_csv.py**, a .py script that compiles annotated data from folders of .ann files to .csv files per emoji per annotator.
3. **batching.py**, a .py script that creates batches of 100 from randomly selected 5000 files from the processed dataset.
4. **create_dataset.py**, a .py script that creates a pre-processed dataset from a given .csv file.
5. **csv_to_ann.py**, a .py script that converts a given .csv file to a folder of .ann files per file line.
6. **csv_to_txt.py**, a .py script that converts a given .csv file to a folder of .txt files per file line.
7. **find_span.py**, a .py script that finds emoji spans in a given .txt file and writes the data into a .csv file.
8. **txt_to_csv.py** a .py script that compiles .txt files to .csv files per emoji per annotator.