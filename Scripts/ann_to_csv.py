import csv
import os


def ann_to_csv(directory: str, annotator: str):
    """
    Compile annotated data from ann files in the given directory to a csv file.

    :param directory: a directory containing directories of annotated data
    :param annotator: the name of the annotator
    """
    emoji_names = ["FHBT", "LCF", "SFWT"]
    for emoji in emoji_names:
        # get name of the csv file
        file_name = os.path.join(directory, annotator, emoji + '.csv')

        main_dir = os.path.join(directory, annotator, emoji)

        # open csv file in append mode
        with open(file_name, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'span', 'sentiment', 'comment'])
            writer.writeheader()

            for file in os.listdir(main_dir):
                with open(os.path.join(main_dir, file), newline='', encoding="utf-8") as f:
                    # a tweet can have more than one span; these lists hold all spans and their data in a single tweet
                    spans = []
                    sentiments = []
                    comments = []

                    # keep track of the tweet id
                    idx = os.path.basename(file).rsplit(".")[0]

                    # only read data from .ann files
                    if f.name[-3:] == "ann":
                        lines = f.readlines()
                        for line in lines:
                            # search for lines that correspond to the emoji spans
                            if line[0] == "T":
                                span_label = line[:2]
                                span_content = line[line.find("Emoji")+6:].strip("\n\r").replace("\t", " ")
                                spans.append(idx + " " + span_label + " " + span_content)
                            # search for lines that correspond to the sentiment attributes selected by the annotators
                            if line[0] == "A":
                                sentiment = line[line.find("T"):].strip("\n").replace("\t", " ")
                                sentiments.append(idx + " " + sentiment)
                            # search for lines that correspond to the notes left by the annotators
                            if line[0] == "#":
                                comment = line[line.find("AnnotatorNotes")+15:].strip("\n").replace("\t", " ")
                                comments.append(idx + " " + comment)

                    # write all data to the csv file
                    for i in range(len(spans)):
                        id_num = spans[i][:spans[i].find("T")]
                        span = spans[i][spans[i].find("T"):]
                        sentiment = get_sentiment(spans[i], sentiments)
                        comment = get_comment(spans[i], comments)
                        writer.writerow({'id': id_num, 'span': span[3:], 'sentiment': sentiment, 'comment': comment})


def get_sentiment(span: str, sentiments: list) -> str:
    """
    Retrieves the sentiment corresponding to the span of interest given a list of sentiments associated with the file
    containing the given span. Returns an empty string if there is no corresponding sentiment.

    Args:
        span: The span of interest
        sentiments: A list of sentiments associated to the file containing the span

    Returns: The sentiment that corresponds to the span of interest
    """
    for sentiment in sentiments:
        sentiment_tag = sentiment.find("T")
        span_tag = span.find("T")

        if sentiment[sentiment_tag:sentiment_tag+2] == span[span_tag:span_tag+2]:
            return sentiment[sentiment_tag+3:]
    return ""


def get_comment(span: str, comments: list) -> str:
    """
    Retrieves the comment corresponding to the span of interest given a list of comments associated with the file
    containing the given span. Returns an empty string if there is no corresponding comment.

    Args:
        span: The span of interest
        comments: A list of comments attached to the file containing the span

    Returns: The comment that corresponds to the span of interest
    """
    for comment in comments:
        comment_tag = comment.find("T")
        span_tag = span.find("T")

        if comment[comment_tag:comment_tag+2] == span[span_tag:span_tag+2]:
            return comment[comment_tag+3:]
    return ""


# change "internal" to "external" when compiling annotated data from external annotators
directory_name = os.path.join(os.path.pardir, "annotated_data", "external")
for annotator_name in os.listdir(os.path.join(directory_name)):
    ann_to_csv(directory_name, annotator_name)
