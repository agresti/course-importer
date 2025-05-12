# course-importer
A Python script that transforms CSV course listings into structured content blocks for use in CMSs, APIs, or headless systems.
---

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
