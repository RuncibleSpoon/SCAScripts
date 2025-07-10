# SCAScripts

A couple of Python scripts for parsing Endor Labs SCA output and comparing it to others. 

Use these in conjunction with Endor Labs SCA to parse API output into a simple CSV and then compare two CSVs.

## Usage

### Take the json output from the API call and turn it into a CSV

api_data_parser.py <input_json_file> <output_csv_file>

### Compare two CSVs containing dependecny, version

compare_csv.py <master.csv> <test.csv>
