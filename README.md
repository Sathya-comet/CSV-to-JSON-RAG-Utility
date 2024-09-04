CSV to JSON RAG Utility
This utility converts CSV and Excel files to JSON format, optimized for Retrieval-Augmented Generation (RAG) systems. It handles multiple input files, supports large datasets, and automatically splits output into multiple files if necessary.
Features

Converts CSV and Excel (.xls, .xlsx) files to JSON
Handles large input files by increasing CSV field size limit
Automatically splits output into multiple JSON files if size exceeds 15MB
Allows adding custom URLs to each entry
Preserves original filename information in the JSON output

Prerequisites
Ensure you have Python installed on your system along with the following libraries:

pandas
openpyxl (for Excel file support)

You can install the required libraries using pip:
Copypip install pandas openpyxl
Usage

Place your CSV and/or Excel files in the ./resources directory.
Run the script:
Copypython csv_to_json_rag.py

For each file, you'll be prompted to enter a URL (optional). Press Enter to skip if no URL is needed.
The script will process each file and generate JSON output in the ./resources directory.
Check the console output for information about the conversion process and where to find the results.

Output

The script generates JSON files named output.json, output1.json, etc., in the ./resources directory.
Each JSON entry contains:

title: The original filename without extension
content: A string containing all the CSV data
url: The URL you provided (if any)
doc_name: The original filename with extension



Notes

The script automatically handles CSV files larger than 15MB by splitting them into multiple output files.
Excel files are temporarily converted to CSV for processing and then deleted.
If you want to append to existing output files, set first_run_flag = False in the script.

Troubleshooting

If you encounter memory errors with large files, try increasing the CSV field size limit in the script.
Ensure you have write permissions in the ./resources directory.

Contributing
Feel free to fork this repository and submit pull requests with any enhancements.
