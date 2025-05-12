import csv
import datetime
import os

class CourseImporter:
    def __init__(self, input_file, output_folder="output"):
        self.input_file = input_file
        self.output_folder = output_folder
        self.course_blocks = []
        self.page_name = f"course-data-{datetime.datetime.now().strftime('%Y-%m-%d')}.json"

    def read_csv(self, delimiter=','):
        """Reads CSV into a list of dictionaries."""
        print("Reading course data...")
        try:
            with open(self.input_file, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                return [row for row in reader]
        except Exception as e:
            print(f"Error reading file: {e}")
            return []

    def sanitize(self, value):
        """Sanitizes text for output."""
        if not value:
            return ""
        return ''.join(c if c.isprintable() else " " for c in value).strip()

    def transform_course(self, course):
        """Converts a course row into structured block."""
        return {
            "type": "group",
            "identifier": "course",
            "fields": [
                {"id": self.write_tag(key), "value": self.sanitize(value)}
                for key, value in course.items()
                if self.is_valid_field(key)
            ]
        }

    def is_valid_field(self, field_name):
        """Placeholder for filtering unwanted fields."""
        valid_fields = ["Course Code", "Title", "Instructor", "Credits", "Description"]
        return field_name in valid_fields

    def write_tag(self, text):
        """Converts a field name into camelCase identifier."""
        parts = text.strip().split()
        return parts[0].lower() + ''.join(p.title() for p in parts[1:])

    def generate_output(self):
        """Writes structured course blocks to a JSON-like output."""
        print("Generating output...")
        os.makedirs(self.output_folder, exist_ok=True)
        path = os.path.join(self.output_folder, self.page_name)

        try:
            with open(path, mode='w', encoding='utf-8') as f:
                for block in self.course_blocks:
                    f.write(str(block) + '\n')
            print(f"Data written to {path}")
        except Exception as e:
            print(f"Failed to write output: {e}")

    def run(self):
        print("Starting course import process...")
        data = self.read_csv()
        self.course_blocks = [self.transform_course(row) for row in data]
        self.generate_output()


if __name__ == "__main__":
    importer = CourseImporter(input_file="courses.csv")
    importer.run()
