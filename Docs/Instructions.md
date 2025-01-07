# **Generating Replicas of Coding Questions**

## **Prerequisites**
To generate replicas, ensure you have the following:
- **Question text** in Markdown format.
- **Difficulty level** of the question.
- **Sub-topic** categorized under the main topic.

---

## **Steps to Follow**

### **Step 1: Navigate to the Directory**
- Go to the `replication_questions` directory. If it is missing create one with the same name in root directory.

### **Step 2: Create the Markdown File** 
- Create a Markdown file in this directory and name it using the following convention:

#### **File Naming Format**
`<question_name>.<difficulty>.<sub_topic>.md`
For example, if:
- Question name: `que-01`
- Difficulty level: `EASY`
- Sub-topic: `DATA_TYPE_LIST`

The filename should be:
`que-01.EASY.DATA_TYPE_LIST.md`


#### **Alternative: Auto-Generate Files Using Python**
Instead of manually creating the files, use the `question_file_creator.py` script:
1. Open `question_file_creator.py` and update the following lists:
   - **`names`** → List of all question names to replicate.
   - **`difficulties`** → Corresponding difficulty levels (same order as `names`).
   - **`sub_topics`** → Corresponding sub-topics (same order as `names`).
2. Run the script. It will create all `.md` files following the naming convention.

### **Step 3: Add Question Content**
- Paste the corresponding question content into the correct Markdown files.

### **Step 4: Validate the Directory**
- Ensure that:
  - No **unnecessary files** exist in the `replication_questions` directory.
  - All file names **follow the defined naming convention**.

### **Step 5: Run the Main File**
- Execute the main script to process the questions.

### **Step 6: Listen for Completion Signal**
- When the process finishes, **three beeps** will sound.

### **Step 7: Collect Output CSVs**
- Navigate to the `csv` directory to retrieve the output files.
- Each CSV contains all generated replicas for a single question.
- **CSV Naming Convention:** The first component of the Markdown filename is used.

### **Step 8: Upload CSVs to Google Sheets**
- Upload the generated CSV files.
- Review each question for correctness:
  - Check the column **`is_valid`**.
  - If `false`, manually review the question and make corrections.

### **Step 9: Convert CSV to JSON**
- Run the **Google App Script** to convert CSV files into JSON format.

### **Step 10: Load JSON to Beta**
- Upload the generated JSON files to the beta environment for further processing.

---
