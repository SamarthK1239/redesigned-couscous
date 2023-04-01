from pathlib import Path

import monkeylearn as monkeylearn
from dotenv import load_dotenv
import os

dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

ml = monkeylearn.MonkeyLearn(os.getenv('api-key'))
model_id = 'cl_pi3C7JiL'


def getSentimentLevel(text):
    data = [text]
    return ml.classifiers.classify(model_id, data)


while True:
    text = input()
    result = getSentimentLevel(text).body
    print_statement = result[0]['classifications'][0]
    scaled_confidence = round(float(print_statement['confidence']) * 10, 1)
    print(print_statement['tag_name'], scaled_confidence)
