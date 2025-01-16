import os
import json
from .gpt_connect import ChatAgent
from .json_to_csv_parser import Parser


class QuestionCurator:
    def __init__(self, api_key, endpoint, model_name, api_version):
        self.API_KEY = api_key
        self.ENDPOINT = endpoint
        self.MODEL_NAME = model_name
        self.API_VERSION = api_version
        self.PARSER = Parser()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))


    def _generate_solutions(self, question, retry_limit=5):
        for i in range(retry_limit+1):
            if i!=0:
                if i==1:
                    print("\nRetrying...")
                print(f"\nAttempt {i}/{retry_limit}\n")

            agent = ChatAgent(self.ENDPOINT, self.API_KEY, self.API_VERSION)
            response_solutions = agent.generate_solutions(self.MODEL_NAME, question)

            agent = ChatAgent(self.ENDPOINT, self.API_KEY, self.API_VERSION)
            response_testcases = agent.generate_testcases(self.MODEL_NAME, question)

            agent = ChatAgent(self.ENDPOINT, self.API_KEY, self.API_VERSION)
            validation_result = agent.validate_solutions(self.MODEL_NAME, question, response_solutions, response_testcases)
            try:
                validation_result = json.loads(validation_result)
            except Exception as e:
                print(validation_result)
                continue
            
            if validation_result.get('result') == 'true':
                print("Validation Successful!")
                return (validation_result, 'true')
            elif i+1 == retry_limit:
                print(f"Validation Failed.\n [REASON]: {validation_result.get('message')}")
                return (validation_result, 'false')
            else:
                print(f"Validation Failed.\n [REASON]: {validation_result.get('message')}")

        return None

    def curate(self, question, filename="", difficulty='EASY', sub_topic='DATA_TYPE_LISTS'):
        agent = ChatAgent(self.ENDPOINT, self.API_KEY, self.API_VERSION)
        curated_question = json.loads(agent.generate_question(self.MODEL_NAME, question))

        response = self._generate_solutions(curated_question.get('content'))
        question_data = {}

        if response is not None:
            question_data[filename] = {
                "question": curated_question.get('content'),
                "short_text": curated_question.get('title'),
                "difficulty": difficulty,
                "subtopic": sub_topic,
                "solutions": response[0]["solutions"],
                "testcases": response[0]["testcases"],
                "is_valid": response[1]
            }


        print('Generating CSV')
        self.PARSER.parse_into_coding_question_csv(question_data, filename, self.BASE_DIR)
            
