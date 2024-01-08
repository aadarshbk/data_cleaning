import pandas as pd

# Read data from CSV file into peoplealsoask DataFrame
peoplealsoask_df = pd.read_csv("filtered_peoplealsoask.csv")

# Extract rows where 'Type' is 'PeopleAlsoAsk_Box'
peoplealsoask_box_df = peoplealsoask_df[peoplealsoask_df['FIELD'].str.lower().str.contains('peoplealsoask_box')]

# Extract only the 'Value' column from PeopleAlsoAsk_Box DataFrame
value_column = peoplealsoask_box_df['VALUE']

# Display the 'Value' column
print("Extracted 'Value' :")
print(value_column)
# Save the 'Value' column to a new CSV file
value_column.to_csv("Peoplealsosearch.csv", index=False)

# Display the saved CSV file
print(f"Extracted 'Value' column saved to 'extracted_value_column.csv'")

