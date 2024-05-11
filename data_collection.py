import pandas as pd
import requests
import time

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64b698652bb7de2cba67e180&org=13898844-5175-468f-911d-416ba3088083"
headers = {'Authorization':
			 'Bearer ### Replace here ###',
			 'Content-Type': 'application/json'
		}



def query(payload, max_retries=3):
    for _ in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        except requests.exceptions.ConnectionError:
            print("Connection error, retrying...")
            time.sleep(2)  # wait for 2 seconds before retrying
    raise RuntimeError("Failed to send request after multiple attempts")


# Function to check if string is ASCII
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# Read the events from a CSV file into a DataFrame with explicit encoding specified
events = pd.read_csv(r'C:\Users\ycohe\Desktop\Work\Empire Media\event file\events_final1.csv', header=None, )

# Select rows where column 1 is null
selected_rows = events.loc[pd.isnull(events[1])]
print(events)
print(selected_rows)

# Iterate over each selected row
for i, (index, row) in enumerate(selected_rows.iterrows()):
    # Send each event to the API
    output = query({"in-0": row[0]})
    print(output)
    # Enter the API response in the row of that event
    if 'out-0' in output and is_ascii(output['out-0']):
        events.loc[index, 1] = output['out-0']
        print("row 0 : " , row[0], "row 1 : " , row[1])

    # After processing each row, save the DataFrame to a CSV file.
    events.to_csv(r'C:\Users\ycohe\Desktop\Work\Empire Media\event file\events_final.csv', index=False, header=False)

    # Also, save the current state to three different backup files.
    events.to_csv(f'C:\\Users\\ycohe\\Desktop\\Work\\Empire Media\\event file\\events_final{i % 3 + 1}.csv', index=False, header=False)

# Print the updated DataFrame
print(events.head())


