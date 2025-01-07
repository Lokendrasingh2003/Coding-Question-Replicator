import os
import shutil

def create(question_name, difficulty, sub_topic):
    output_folder = "replication_questions"

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)


    for part1, part2, part3 in zip(question_name, difficulty, sub_topic):
        filename = f"{part1}.{str(part2).upper()}.{str(part3).upper()}.md"
        file_path = os.path.join(output_folder, filename)

        # Create an empty file
        with open(file_path, "w") as file:
            pass

        print(f"Created: {file_path}")

if __name__ =='__main__':
    name = ["Que 07", "Que 08", "Que 09"]
    difficulties = ["MEDIUM", "HARD", "HARD"]
    sub_topics = ["DATA_TYPE_LIST", "DATA_TYPE_LIST", "DATA_TYPE_LIST"]

    create(name, difficulties, sub_topics)