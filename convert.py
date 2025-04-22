# Convert the emails in the csv file to a text file: one file per row

import csv
import os

def generate_email_files(input_path, output_path):
    # Make sure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader, start=1):
            subject = row.get('subject', '').strip()
            body = row.get('body', '').strip()
            
            filename = f"BEC-2-{i}."
            filepath = os.path.join(output_path, filename)
            
            with open(filepath, 'w', encoding='utf-8') as outfile:
                outfile.write(f"Subject: {subject}\n\n{body}")

# Example usage
input_path = './data/BEC-2-human.csv'
output_path = './data/BEC-2-emails'  # Output directory for email files
generate_email_files(input_path, output_path)
