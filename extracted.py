import pandas as pd

# Read data from CSV file into peoplealsoask DataFrame
RelatedSearches_df = pd.read_csv("filtered_RelatedSearches.csv")

# Extract rows where 'Type' is 'PeopleAlsoAsk_Box'
RelatedSearches_Text_df = RelatedSearches_df[RelatedSearches_df['FIELD'].str.lower().str.contains('relatedsearches_text')]

# Extract only the 'Value' column from PeopleAlsoAsk_Box DataFrame
value_column = RelatedSearches_Text_df['VALUE']

# Display the 'Value' column
print("Extracted 'Value' :")
print(value_column)
# Save the 'Value' column to a new CSV file
value_column.to_csv("Related.csv", index=False)

# Display the saved CSV file
print(f"Extracted 'Value' column saved to 'extracted_value_column.csv'")

