from dotenv import load_dotenv
import os
import winsound
import time
import logging
import sys

from process_automation.curator import QuestionCurator
from process_automation.replicator import QuestionReplicator
from log_handler import LoggerWriter


load_dotenv()

API_KEY = os.getenv('key')
END_POINT = os.getenv('endpoint')
MODEL_NAME = os.getenv('model_name')
API_VERSION = os.getenv('api_version')

sys.stdout = LoggerWriter(logging.info)
sys.stderr = LoggerWriter(logging.error)



def get_contexts():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    os.makedirs('curation_contexts', exist_ok=True)

    directory = os.path.join(current_directory, 'curation_contexts')

    files = [f for f in os.listdir(directory) if f.endswith('.md')]

    questions_data = []

    for file in files:
        q_data = {}
        with open(os.path.join(directory, file), 'r') as f:
            q_data['context'] = f.read()
            q_data['file_name'] = file.split('.')[0]
            q_data['difficulty'] = file.split('.')[1].upper()
            q_data['sub_topic'] = file.split('.')[2].upper()
            questions_data.append(q_data)

    return questions_data


if __name__ == '__main__':
    curator = QuestionCurator(API_KEY, END_POINT, MODEL_NAME, API_VERSION)

    for question_context in get_contexts():
        if question_context.get('context').strip() != "":
            print(f"Working on {question_context.get('file_name')} ...")
            curator.curate(question_context.get('context'), question_context.get('file_name'), question_context.get('difficulty'), question_context.get('sub_topic'))

    for i in range(3):
        winsound.Beep(1300, 400)
        time.sleep(0.1)

