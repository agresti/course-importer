# course-importer

A Python script that simulates importing course data from a `.csv` file and converting it into a structured block format — suitable for use in content systems, headless CMS, or static site generators.

## 📌 Features

- Reads and sanitizes CSV course data
- Filters only relevant fields
- Outputs a structured block format (JSON-like)
- Uses camelCase identifiers
- Logs progress in the terminal
- Safe for sharing and customization

---

## 📁 Files

| File              | Description                                 |
|-------------------|---------------------------------------------|
| `course_importer.py` | Main Python script                         |
| `courses.csv`         | Example input data in CSV format           |
| `output/`             | Output folder for the transformed content |

---

## 🔧 How to Use

1. Clone or download this repo.
2. Make sure Python 3.6+ is installed.
3. Run the script:
   ```bash
   python course_importer.py
