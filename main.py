import pandas as pd
import json
import os

def excel_to_json(excel_file, sheet_name=None):
    try:
        # Read Excel file
        if sheet_name:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
        else:
            df = pd.read_excel(excel_file)
        
        # Convert DataFrame to JSON with line-separated records
        json_data = df.to_json(orient='records', lines=True)
        
        return json_data
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    # Ask user for the Excel file path
    excel_file_path = input("Enter the path to the Excel file: ")
    
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(excel_file_path))[0]
    
    # Example usage
    json_data = excel_to_json(excel_file_path)
    if json_data:
        output_file_path = f"{file_name}.json"
        with open(output_file_path, 'w') as f:
            f.write(json_data)
        print(f"Conversion was successful. JSON data written to {output_file_path}.")
