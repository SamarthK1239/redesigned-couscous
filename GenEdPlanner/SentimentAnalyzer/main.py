from pathlib import Path

import monkeylearn as monkeylearn
from dotenv import load_dotenv
import os
import scrape_reddit

dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

ml = monkeylearn.MonkeyLearn(os.getenv('api-key'))
model_id = 'cl_pi3C7JiL'


def getSentimentLevel(text):
    data = [text]
    return ml.classifiers.classify(model_id, data)


def scaledRecommendation(query):
    comments_list = scrape_reddit.get_comments_list(query)
    weights_list = []

    for i in comments_list:
        multiplicative_factor = 1

        try:
            result = getSentimentLevel(i).body
            print_statement = result[0]['classifications'][0]
            scaled_confidence = round(float(print_statement['confidence']) * 10, 1)

            if print_statement['tag_name'] == "Positive":
                multiplicative_factor = 1
            elif print_statement['tag_name'] == "Negative":
                multiplicative_factor = -1

            scaled_confidence = multiplicative_factor * scaled_confidence
            #print(print_statement, scaled_confidence)

            weights_list.append(scaled_confidence)

            if print_statement['tag_name'] == "Neutral":
                weights_list.pop()

            mean = sum(weights_list) / len(weights_list)
            '''
            if mean > 0:
                print("Overall Positive, Score of: " + str(mean))
            elif mean < 0:
                print("Overall Negative, Score of: " + str(mean))
            else:
                print("Neutral Opinion, defer to your own judgement")
            '''
            return mean
        except:
            pass
