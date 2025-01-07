import os


class Prompt:

    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def prompt_for_solution(self, question):
        with open(os.path.join(self.BASE_DIR, 'prompts', 'generate_solution.txt'), 'r') as f:
            return f'{f.read()}\n{question}'

    def prompt_for_testcases(self, question):
        with open(os.path.join(self.BASE_DIR, 'prompts', 'generate_testcases.txt'), 'r') as f:
            return f'{f.read()}\n{question}'

    def prompt_for_variants(self, question):

        with open(os.path.join(self.BASE_DIR, 'prompts', 'generate_replica.txt'), 'r') as f:
            return f.read().format(QUESTION=question)
        
    def prompt_for_validation(self, question, solutions, testcases):
        with open(os.path.join(self.BASE_DIR, 'prompts', 'validate_solution.txt'), 'r') as f:
            return f.read().format(QUESTION=question, SOLUTIONS=solutions, TESTCASES=testcases)


if __name__ == "__main__":
    prompt = Prompt()
    print('Testing...')
    print(prompt.prompt_for_solution("Given a list of numbers, find the maximum subarray sum"), '\n')
    print(prompt.prompt_for_testcases("Given a list of numbers, find the maximum subarray sum"), '\n')
    print(prompt.prompt_for_variants("Given a list of numbers, find the maximum subarray sum"), '\n')
    print(prompt.prompt_for_validation("Given a list of numbers, find the maximum subarray sum", "SOLUTIONS", "TESTCASES"))
