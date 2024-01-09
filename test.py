import pandas as pd
import json
from sqlalchemy import create_engine

def custom_data(custom_list):
    print("Extracting custom data ...") 
    df = pd.read_csv("vertical.tsv", sep='\t')
    field = df.columns[2]
    
    df_custom_data = []
    for text in custom_list:
        # filtered_df = df[df[field].str.contains(text, case=False, na=False)]
        filtered_df = df[df[field].str.contains(text, na=False)]
        df_custom_data.append(filtered_df)
        
    df_custom_data = pd.concat(df_custom_data)
    # print(df_custom_data)
    print("Custom data successfully extracted.")
    return df_custom_data
        
def extract_json(df):
    print("Creating dataframe ...")
    df_groups = df.groupby("SystemId")
    custom_data = []
    for sys_id, sub_df in df_groups:
        sub_df.set_index('FIELD', inplace=True)
        df_subgroups = sub_df.groupby("FIELD")
        datas = {
            "SystemId": sys_id
        }
        test_list = []
        for key, req_df in df_subgroups:
            # print(f"field = {key}")
            # print(req_df)
            req_df.reset_index(inplace = True)
            df1 = pd.DataFrame()
            df1[key] = req_df['VALUE']
            # df2 =df1.pivot(columns='FIELD')
            # print(df1)
            test_list.append(df1)
        df_one = pd.concat(test_list, axis=1)
        # print(df_one)
        custom_data.append(df_one)
    df_final = pd.concat(custom_data, axis=0)
    print("Dataframe successfully created.")
    return df_final
    
def load_to_database(custom_list):
    print("Creating Table ...")
    # df = pd.read_json(file)
    df = pd.DataFrame(custom_list)
    engine = create_engine("postgresql://postgres:12345@localhost:5432/postgres")
    
    with engine.connect() as conn:
        df.to_sql('my_table', con=engine, if_exists='replace')
        conn.commit()
        
    print("Table successfully created.")


custom_list = ["PeopleAlsoAsk_QuestionText", "PeopleAlsoAsk_QuestionLandingLink","Organic_Title", "Organic_LandingLink", "Organic_ReviewCount", "Organic_Price", "Organic_Rating"]
df_custom_data = custom_data(custom_list)
df_table = extract_json(df_custom_data)
load_to_database(df_table)