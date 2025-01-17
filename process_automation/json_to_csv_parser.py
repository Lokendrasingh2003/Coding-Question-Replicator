import csv
import os


class Parser:
    def __init__(self):
        pass

    def parse_into_coding_question_csv(self, json_data, filename, base_dir, testcase_count=10):

        lang_sequence = {
            "python": 0,
            "java": 1,
            "cpp": 2,
            "c": 3,
        }

        headers = ["S. No",	"Difficulty", "Question Content (in Markdown)",	"Question_short_text", "Sub_Topics", "Code_language", "Solution Code", "Front_Code_language", "Prefilled Code For Each Code Language", "Test_case_input", "Test_case_output", "Test_case_type",	"Code_language", "Backend Code", "is_valid"]
        rows = []
        sr_no = 0
        for key in json_data.keys():
            sr_no += 1
            testcases = json_data[key]['testcases']
            row = [[""]*(len(headers)) for _ in range(min(testcase_count,len(testcases))+2)]
            row[0] = [f"{sr_no}", json_data[key].get('difficulty', 'EASY'), json_data[key].get('question', ""), json_data[key].get('short_text', ""), json_data[key].get('sub_topic', 'DATA_TYPE_LIST'), "", "", "", "", "", "", "", "", "", json_data[key].get('is_valid')]

            for k in json_data[key]['solutions'].keys():
                solutions = json_data[key].get('solutions').get(k)
                if k == "python":
                    row[lang_sequence[k]][5] = str(k).upper()
                    row[lang_sequence[k]][6] = solutions.get('solution_code', "")

                row[lang_sequence[k]][7] = str(k).upper()
                row[lang_sequence[k]][8] = solutions.get('prefilled_code', "")

                if solutions.get('backend_code', "") != "":
                    row[lang_sequence[k]][12] = str(k).upper()
                    row[lang_sequence[k]][13] = solutions.get('backend_code', "")

            testcases = json_data[key]['testcases']
            for i in range(min(testcase_count,len(testcases))):
                row[i+1][9] = testcases[i].get('input', "")
                row[i+1][10] = testcases[i].get('output', "")
                row[i+1][11] = testcases[i].get('testcase_type', "")
            
            rows.extend(row)

        os.makedirs('csv', exist_ok=True)
        with open(os.path.join(os.path.dirname(base_dir), 'csv', f"{filename}.csv"), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
            print(f"CSV file {os.path.join(os.path.dirname(base_dir), 'csv', f"{filename}.csv")} generated successfully.")

