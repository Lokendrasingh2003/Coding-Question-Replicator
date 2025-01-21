from openai import AzureOpenAI
from dotenv import load_dotenv
from .gpt_prompt import Prompt

load_dotenv()


class ChatAgent:

    def __init__(self, end_point, key, version):

        self.client = AzureOpenAI(azure_endpoint=end_point, api_key=key, api_version=version)
        self.prompt = Prompt()
        
    def generate_solutions(self, model, question):

        print("Requesting GPT to generate solutions")

        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": self.prompt.prompt_for_solution(question=question),
                },
            ]
        )
        print("Solutions generated")
        return completion.choices[0].message.content

    def generate_testcases(self, model, question):

        print("Requesting GPT to generate test cases")

        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": self.prompt.prompt_for_testcases(question=question),
                },
            ]
        )

        print("Testcases generated")
        return completion.choices[0].message.content
        
    def validate_solutions(self, model, question, solutions, testcases):

        print("Requesting GPT to validate solutions")

        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": self.prompt.prompt_for_validation(question, solutions, testcases),
                }
            ]
        )

        return completion.choices[0].message.content
        
    def generate_replica(self, model, question):

        print("\nRequesting GPT to Replicate Question")


        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": self.prompt.prompt_for_variants(question),
                }
            ]
        )
        print("Question Replicated")
        return completion.choices[0].message.content

    def generate_question(self, model, question):

        print("\nRequesting GPT to Curate Question")


        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": self.prompt.prompt_for_question(question),
                }
            ]
        )
        print("Question Curated")
        return completion.choices[0].message.content
