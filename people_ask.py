import pandas as pd

# Read data from TSV file into peoplealsoask DataFrame
peoplealsoask_df = pd.read_csv("vertical.tsv", sep='\t')

# Filter rows based on the 'FIELD' column containing 'peoplealsoask'
filtered_peoplealsoask_df = peoplealsoask_df[peoplealsoask_df['FIELD'].str.lower().str.contains('peoplealsoask')]

# Display the filtered DataFrame
print("Filtered PeopleAlsoAsk DataFrame:")
print(filtered_peoplealsoask_df)

# Save the filtered PeopleAlsoAsk DataFrame to a CSV file
filtered_peoplealsoask_df.to_csv("filtered_peoplealsoask.csv", index=False)

# Display a message indicating that the CSV file has been saved
print(f"Filtered PeopleAlsoAsk DataFrame saved to 'filtered_peoplealsoask.csv'")

# Read data from TSV file into RelatedSearches DataFrame
RelatedSearches_df = pd.read_csv("vertical.tsv", sep='\t')

# Filter rows based on the 'FIELD' column containing 'relatedsearches'
filtered_RelatedSearches_df = RelatedSearches_df[RelatedSearches_df['FIELD'].str.lower().str.contains('relatedsearches')]

# Display the filtered DataFrame
print("Filtered RelatedSearches DataFrame:")
print(filtered_RelatedSearches_df)

# Save the filtered RelatedSearches DataFrame to a CSV file
filtered_RelatedSearches_df.to_csv("filtered_RelatedSearches.csv", index=False)

# Display a message indicating that the CSV file has been saved
print(f"Filtered RelatedSearches DataFrame saved to 'filtered_RelatedSearches.csv'")

# (Optional) Repeat the operations for PeopleAlsoAsk data
peoplealsoask_df = pd.read_csv("vertical.tsv", sep='\t')
filtered_peoplealsoask_df = peoplealsoask_df[peoplealsoask_df['FIELD'].str.lower().str.contains('peoplealsoask')]

# Display the filtered DataFrame
print("Filtered PeopleAlsoAsk DataFrame:")
print(filtered_peoplealsoask_df)

# Save the filtered PeopleAlsoAsk DataFrame to a CSV file
filtered_peoplealsoask_df.to_csv("filtered_peoplealsoask.csv", index=False)
