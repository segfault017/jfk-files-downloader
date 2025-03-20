import wget
import csv
import os

rootPath = "https://www.archives.gov/files/research/jfk/releases/2025/0318/"

# Create files directory if it doesn't exist
os.makedirs('./files', exist_ok=True)

with open('file-names.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        filename = row[0].strip()
        if filename:  # Skip empty lines
            url = rootPath + filename
            try:
                wget.download(url, out='./files')
                print(f"\nDownloaded {filename}")
            except Exception as e:
                print(f"\nError downloading {filename}: {e}")

