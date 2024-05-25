# SWiT: Emoji Annotation

**Authors:** Emily Braun, Joyce Guo, Kasey La, Keer Xu

This is our semester group project for Natural Language Annotation for Machine Learning (COSI 230b) where students 
have the opportunity to apply natural language annotation skills learned throughout the semester. After forming groups,
our tasks are to create a dataset, perform pre-processing on the collected dataset, write and revise annotation
guidelines following the MAMA (Model-Annotate-Model-Annotate) cycle, retrieve annotated data from internal and external
annotation, report inter-annotator agreement, train a model on our annotated dataset, and write a paper and present
the process of the project throughout the semester.

For our project, we are observing the sentiment of three emojis that can be found in both positive and negative
contexts:
1. 🥹 - face holding back tears (FHBT)
2. 😭 - loudly crying face (LCF)
3. 🥲 - smiling face with tear (SFWT)

More information, including the motivation for this project, can be found in our annotation guidelines.

### Contents of this folder
This folder contains 11 files:

1. This **README** file.
2. **annotated_data**, a folder containing annotated data collected internally and externally.
3. **old_files**, a folder containing old files used for internal annotation.
4. **original_data**, a folder containing the original datasets from [Kaggle](https://www.kaggle.com/datasets/ericwang1011/tweets-with-emoji).
5. **processed_data**, a folder containing the pre-processed dataset, where the data is presented in .csv format and in folders of .txt files.
6. **scripts**, a folder containing .py scripts used to create the files for this project.
7. **Annotation guidelines v2.pdf**, a document outlining our goals, the classification task, and the annotation guidelines for our task.
8. **SWiT Emoji Sentiment Brat Setup & Tutorial (External).pdf**, a document containing the instructions for setup and annotating in BRAT.
9. **SWiT Final Paper.pdf**, a document reporting our project in detail, including our computed Inter-Annotator Agreement score and machine learning baseline.
10. **swit_files.zip**, a zipped folder containing data and configuration files to be annotated and opened in BRAT.
11. **replication.zip**, a zipped folder containing the files necessary for replicating this project.

### Instructions for external annotators
Please download **swit_files.zip** and follow the instructions outlined in
**SWiT Emoji Sentiment Brat Setup & Tutorial (External).pdf**. During the annotation process, please refer to
**Annotation guidelines v2.pdf** and reach out to us with any questions.

If you would like to access these documents on Google Docs, you can find the links below:
* [SWiT Emoji Sentiment Brat Setup & Tutorial (External)](https://docs.google.com/document/d/1i1rDM1SpTKDrYlRSehMHeAcm__Ph2wM4MVowN1pWvdc/edit?usp=sharing)
* [Annotation guidelines v2](https://docs.google.com/document/d/1fGMEWfhTian-0fDZOx7am2xDAyuLTEfL1RAUE2G7kUc/edit?usp=sharing)

### Instructions for replicating this project
To replicate this project, follow the instructions below:
1. Download **replication.zip**, which contains the original data, scripts to be run, and configuration files along with empty directories.
2. Run **create_dataset.py** to preprocess the original data.
3. Run **csv_to_txt.py** to create .txt files from the preprocessed data.
4. Run **find_span.py** to retrieve the spans in each .txt file.
5. Run **csv_to_ann.py** to create .ann files using the spans found.
6. Run **batching.py** to create a smaller randomized batch of data for annotation.
7. Send the created **swit_files** directory either as is or zipped to annotators.
8. After collecting data from annotators, upload each folder into the **annotated_data** directory. Remove excess files aside from the three emoji directories (FHBT, LCF, SFWT).
9. Run **txt_to_csv.py** and **ann_to_csv.py** to compile the annotated data.