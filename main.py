import pandas as pd
import json

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

# Example usage
if __name__ == "__main__":
    excel_file_path = 'example.xlsx'  # Provide the path to your Excel file
    json_data = excel_to_json(excel_file_path)
    if json_data:
        with open('output.json', 'w') as f:
            f.write(json_data)
        print("Conversion successful. JSON data written to output.json.")
