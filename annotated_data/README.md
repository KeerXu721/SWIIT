# SWiT: Emoji Annotation Annotated Data

**Author:** Kasey La

This folder contains 7 files:

1. This **README** file.
2. **external**, a folder containing annotated data collected externally (outside our group).
3. **internal**, a folder containing annotated data collected internally (within our group).
4. **data-external.csv**, a file containing annotated data collected externally.
5. **data-gold.csv**, a file containing our gold data, collected when we made our guidelines.
6. **data-internal.csv**, a file containing annotated data collected internally.
7. **dataset.csv**, a file containing all data collected: gold, internal, and external.

Within both the **external** and **internal** folders, each folder corresponding to an annotator contains:

1. **FHBT**, a folder containing .txt files and .ann files for the tweets whose main emoji is 🥹.
2. **LCF**, a folder containing .txt files and .ann files for the tweets whose main emoji is 😭.
3. **SFWT**, a folder containing .txt files and .ann files for tweets whose main emoji is 🥲.
4. **FHBT.csv**, a file containing the compiled tweet ID, emoji span, annotated sentiment, and comment for the FHBT tweets.
5. **LCF.csv**, a file containing the compiled tweet ID, emoji span, annotated sentiment, and comment for the LCF tweets.
6. **SFWT.csv**, a file containing the compiled tweet ID, emoji span, annotated sentiment, and comment for the SFWT tweets.

Within just the **external** folder, each folder corresponding to an annotator also contains:

1. **FHBT-tweets.csv**, a file containing the compiled tweet ID and text for the FHBT tweets.
2. **LCF-tweets.csv**, a file containing the compiled tweet ID and text for the LCF tweets.
3. **SFWT-tweets.csv**, a file containing the compiled tweet ID and text the SFWT tweets.