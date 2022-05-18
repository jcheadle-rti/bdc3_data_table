import json
import csv
from datetime import datetime

'''
Set values here
'''
input_filepath = "inputs/COVID Study Table - Update JAN 2022.csv" # input CSV filepath
table_type = "covid" # Either 'studies' or 'covid'
today = datetime.today().strftime("%Y-%m-%d")
output_filepath = f"outputs/data_table_{table_type}_{today}.json" # output path

def main(input_filepath = input_filepath, table_type = table_type, output_filepath = output_filepath):
    # Convert CSV to JSON
    input_json = csv_to_json(input_filepath)

    # Changes names for output
    if table_type=="studies":
        print(table_type)
        output_json = studies_table(input_json)

    elif table_type=="covid":
        print(table_type)
        output_json = covid_table(input_json)

    else:
        print("Invalid table_type.  Please check the script entry.")
        exit()

    # Create output
    with open(output_filepath, "w") as stream:
        json.dump(output_json, stream, indent=2)

def csv_to_json(input_filepath):
    input_json = []
      
    #read csv file
    with open(input_filepath, encoding='utf-8-sig') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            input_json.append(row)
    
    return(input_json)

def studies_table(input_json):
    studies = input_json
    new_json = []

    for study in studies:
        # strip newlines
        num_vars = study.pop('Total Number of Variables')
        new_study = {k: v.strip() for k, v in study.items() if isinstance(v, str)}
        
        # Change Names
        new_study['Accession'] = new_study.pop('Study Accession')
        new_study['Cohort Abbreviation'] = new_study.pop('Study - Cohort Abbreviation')
        new_study['Name'] = new_study.pop('Study Name (dbGaP Link)')
        new_study['Description'] = new_study.pop('Study Description (Verbose)')
        new_study['Short Description'] = new_study.pop('Study Description (Short)')
        new_study['Number of Variables'] = num_vars
        new_study['Data Dictionary Link'] = new_study.pop('Primary Data Dictionary Link')
    
        # Change Items
        new_study['dbGaP Listed Variable'] = [new_study.pop('dbGaP Listed Variable')] # just make this a list?
        new_study['Type'] = [new_study.pop('Study Type')] # just make this a list?
        new_study['Populations'] = [x.strip() for x in new_study.pop('Study-Reported Population(s)').split(";")] # semicolon-delimited
        new_study['Molecular Data'] = [x.strip() for x in new_study.pop('Type of Molecular Data Available').split(";")] # semicolon-delimited
        new_study['Consent'] = [x.strip() for x in new_study.pop('Study Consent').split(";")] # semicolon-delimited
        new_study['Consent Short'] = [x.strip() for x in new_study.pop('Consent Short').split(";")]  # semicolon-delimited

        # Append to new table
        new_json.append(new_study)
    
    return(new_json)

def covid_table(input_json):
    studies = input_json
    new_json = []

    for study in studies:
        # strip newlines
        new_study = {k: v.strip() for k, v in study.items() if isinstance(v, str)}
        
        # Change Names
        new_study['Name'] = new_study.pop('Study Title')
        new_study['Short Name'] = new_study.pop('Study Short Name')
        new_study['Description'] = new_study.pop('Study Description')
        new_study['Type'] = new_study.pop('Study Type')
        new_study['Link'] = new_study.pop('Link to Study Landing Page')
        new_study['Network'] = new_study.pop('Link to Organizational Network')

        # Append to new table
        new_json.append(new_study)
    
    return(new_json)

if __name__ == "__main__":
    main()

