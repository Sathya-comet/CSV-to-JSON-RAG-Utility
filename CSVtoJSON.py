#!/usr/bin/env python3

import os
import csv
import json
import time
import pandas as pd
from pathlib import Path

# Increase the CSV field size limit
csv.field_size_limit(int(1e6))  # Increase to 1 million characters

def excel_to_csv(excel_file):
    try:
        df = pd.read_excel(excel_file)
        df = df.map(str)
        csv_file = excel_file.parent / f"{excel_file.stem}.csv"
        
        try:
            df = df.drop(['Unnamed: 0'], axis=1)
            df.to_csv(csv_file, index=False)      
        except:
            df.to_csv(csv_file, index=False)
            
        if csv_file.exists():
            return csv_file, excel_file.suffix
        else:
            return
            
    except Exception as e:
        return f"An error occurred: {str(e)}"

def csv_to_json(csv_file, url, conversion_ext, first_run_flag):
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                json_row = {}
                content = ', '.join([f"{key} : {value}" for key, value in row.items()])
                try:
                    raw_title = csv_file.name
                except:
                    raw_title = str(csv_file).split('\\')[-1]
                doc_name = raw_title.split(".")[0] + conversion_ext
                json_row['title'] = raw_title.split(".")[0]
                json_row['content'] = content
                json_row['url'] = url
                json_row['doc_name'] = doc_name
                
                data.append(json_row)
        
        output_file_path = r"./resources/output.json"
        file_index = 0
        
        while True:
            if file_index > 0:
                output_file_path = f"./resources/output{file_index}.json"
            
            if first_run_flag or not Path(output_file_path).is_file():
                existing_data = []
            else:
                with open(output_file_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            
            new_data = existing_data + data
            json_data = json.dumps(new_data, indent=4)
            
            if len(json_data.encode('utf-8')) <= 15 * 1024 * 1024:  # 15 MB in bytes
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(json_data)
                break
            else:
                if existing_data:
                    # If the file already exists and adding new data exceeds 15 MB,
                    # we keep the existing data and move to a new file
                    file_index += 1
                else:
                    # If it's a new file and data alone exceeds 15 MB,
                    # we need to split the data
                    split_point = len(data) // 2
                    with open(output_file_path, 'w', encoding='utf-8') as f:
                        json.dump(data[:split_point], f, indent=4)
                    data = data[split_point:]
                    file_index += 1
        
        return file_index
    
    except Exception as e:
        print(f"An error occurred while processing {csv_file}: {str(e)}")
        return 0

def main():
    st_time = time.time()
    first_run_flag = True  # Make this as False if you want to keep contents in output.json
    csv_folder = Path(r"./resources")
    last_file_index = 0

    for csv_path in csv_folder.glob("*"):
        if csv_path.suffix.lower() in ['.csv', '.xls', '.xlsx']:
            url = input(f"\nPlease enter the URL for {csv_path.name} (press Enter to skip): ").strip()
            if csv_path.suffix == '.csv':
                try:
                    df = pd.read_csv(csv_path)
                    df.to_csv(csv_path, index=False)
                    last_file_index = csv_to_json(csv_path, url, ".csv", first_run_flag)
                except Exception as e:
                    print(f"Error processing {csv_path}: {str(e)}")
            elif csv_path.suffix in ['.xls', '.xlsx']:
                result = excel_to_csv(csv_path)
                if isinstance(result, tuple):
                    csv_path, conversion_flag = result
                    if csv_path and conversion_flag:
                        last_file_index = csv_to_json(csv_path, url, conversion_flag, first_run_flag)
                        os.remove(csv_path)
                else:
                    print(result)  # Print the error message
            first_run_flag = False
            print(f"\nConversion of {csv_path.name} is successful")

    ed_time = time.time()
    tot_time = ed_time - st_time
    print("\n\nSuccessfully converted csv data to json in {:.2f} seconds!".format(tot_time))
    print("--------------------------------------------")
    if last_file_index == 0:
        print("Check: resources\\output.json for results!")
    else:
        print(f"Check: resources\\output.json to resources\\output{last_file_index}.json for results!")
    print("\n")

if __name__ == "__main__":
    main()