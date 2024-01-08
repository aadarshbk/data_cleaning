import pandas as pd
from sqlalchemy import create_engine

# Read data from CSV files into DataFrames
peoplealsoask_df = pd.read_csv("Peoplealsosearch.csv")
relatedsearches_df = pd.read_csv("Related.csv")

# Combine DataFrames into a single DataFrame with meaningful column names
#my name is AAdarsh, I am a NERD
combined_df = pd.DataFrame()
combined_df['peoplealsoask_value'] = peoplealsoask_df['VALUE']
combined_df['relatedsearches_value'] = relatedsearches_df['VALUE']

# Display the combined DataFrame
# print(combined_df)

# Construct the connection string
conn_str = 'postgresql://postgres:12345@localhost:5432/postgres'

# Create an SQLAlchemy engine
engine = create_engine(conn_str)

# Insert data from the combined DataFrame into the PostgreSQL database
combined_df.to_sql(name='combined_table', con=engine, if_exists='replace', index=False)

print("Data inserted into PostgreSQL database successfully.")
