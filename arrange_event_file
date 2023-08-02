import pandas as pd
import numpy as np

# Function to check if string is ASCII
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def are_all_words_in_s1_in_s2(s1, s2):
    """
    Check if all words of s1 appear in s2, regardless of order or positioning.
    """
    s1_words = set(s1.lower().replace('-', ' ').split())
    s2_words = set(s2.lower().replace('-', ' ').split())

    return s1_words.issubset(s2_words)

# Read CSV files
original_data = pd.read_csv(r'C:\Users\ycohe\Desktop\Work\Empire Media\event file\first_100.csv', header=None, encoding='latin-1')
additional_data = pd.read_csv(r'C:\Users\ycohe\Desktop\Work\Empire Media\event file\to_add.csv', header=None, encoding='latin-1')

# Filter out non-ASCII strings
ascii_filtered_original_data = original_data[original_data[0].apply(is_ascii)]
ascii_filtered_additional_data = additional_data[additional_data[0].apply(is_ascii)]

# Add a new column for the matching string in the original data
ascii_filtered_original_data['matching_string'] = np.nan

# For each row in original_data
for orig_index, orig_row in ascii_filtered_original_data.iterrows():
    matching_string = ''

    # For each row in additional_data
    for add_index, add_row in ascii_filtered_additional_data.iterrows():
        if are_all_words_in_s1_in_s2(str(orig_row[0]), str(add_row[0])):
            matching_string = add_row[0]

    # Set the matching string found in the new column
    if matching_string:
        print(f"Updating row {orig_index} with matching string: {matching_string}")
        ascii_filtered_original_data.at[orig_index, 'matching_string'] = matching_string

# Export the resulting DataFrame to CSV
ascii_filtered_original_data.to_csv(
    r'C:\Users\ycohe\Desktop\Work\Empire Media\event file\merge_chat_output_final.csv', index=False, header=False)
