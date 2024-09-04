# CSV and Excel to JSON Converter

This tool allows you to convert CSV and Excel files to JSON format required by Search Assist's structured data.

## Getting Started

Follow these steps to use the converter:

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
```

### Step 2: Install Dependencies

Ensure you have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).

Navigate to the project directory and install the required Python packages using pip:

```bash
pip install pandas
```

### Step 3: Prepare Your Data

* Place your CSV and Excel files in the `resources` folder within the project directory. Each file will be converted to JSON format.

* please remove the sample CSVs and Excel files ( `Employee Sample Data.csv` , `Financials Sample Data.xlsx`)before adding yours .

### Step 4: Run the Converter

Run the converter script by executing the following command in your terminal or command prompt:

```bash
python converter.py
```

### Follow the prompts to enter the URL for each file (optional). Press Enter to skip if no URL is available.

URL is essentially the address to your file, especially if it's stored online and accessible to others. If your files are hosted anywhere on the internet, you can simply copy and paste the link here!

### Step 5: Check the Output

Once the conversion process is complete, you'll find the converted JSON data in the `output.json` file located in the `resources` folder.

## Additional Notes

- If a CSV file contains Excel-formatted data, the converter will automatically convert it to CSV format before converting it to JSON.
- The converted CSV file will be deleted after conversion to save space.

---

### Further Steps :

you can either ingest or simply upload this `output.json` to Search assist structured data, to make your SA app to answer from your CSVs or excel(xls and xlsx).