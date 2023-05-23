import json
import pandas as pd


def read_jsonl(path):
    # Open the JSONL file
    with open(path, 'r') as file:
        data_list = []
        
        # Read each line in the file
        for line in file:
            # Parse the JSON data from each line
            data = json.loads(line)
            
            # Append the JSON data to the list
            data_list.append(data)

    # Create a Pandas DataFrame from the list of JSON objects
    df = pd.DataFrame(data_list)
    return df