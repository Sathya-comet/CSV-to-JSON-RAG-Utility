import os
import csv
import json
import time
import pandas as pd
from pathlib import Path

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


def csv_to_json(csv_file, url, conversion_ext,first_run_flag):

    with open(csv_file, 'r') as f:
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
    
    output_file_path = r"./resources\output.json"
    
    if first_run_flag:
        existing_data = []  # Clear existing data if it's the first run
    else:
        if Path(output_file_path).is_file() and Path(output_file_path).stat().st_size > 0:
            with open(output_file_path, 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []
    
    existing_data.extend(data) 

    with open(output_file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

if __name__ == "__main__":
    
    st_time = time.time()
    
    first_run_flag = True # Make this as False if you want to keep contents in output.json
    
    csv_folder = Path(r"./resources")
    
    for csv_path in csv_folder.glob("*"):
        if csv_path.suffix.lower() in ['.csv', '.xls', '.xlsx']:
            url = input(f"\nPlease enter the URL for {csv_path.name} (press Enter to skip): ").strip()
            if csv_path.suffix == '.csv':
                df = pd.read_csv(csv_path)
                df = df.map(str)
                df.to_csv(csv_path,index=False)
                csv_to_json(csv_path, url, ".csv",first_run_flag)
                
            
            elif csv_path.suffix == '.xls' or csv_path.suffix == '.xlsx':
                csv_path, conversion_flag = excel_to_csv(csv_path)
                if csv_path and conversion_flag:
                    csv_to_json(csv_path, url, conversion_flag,first_run_flag)
                    os.remove(csv_path)
                    
            first_run_flag = False
                    
    
            print(f"\nConversion of {csv_path.name} is succesfull")
    ed_time = time.time()
    tot_time = ed_time - st_time
    print("\n\nSuccesfully converted csv data to json in {:.2f} seconds!\n--------------------------------------------\nCheck : resources\\output.json for results !\n\n".format(tot_time))
    