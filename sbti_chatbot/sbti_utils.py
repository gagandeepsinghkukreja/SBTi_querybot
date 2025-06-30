
import pandas as pd

def load_sbti_data(filepath="full_by_company.xlsx"):
    df = pd.read_excel(filepath, engine="openpyxl")
    return df

def get_company_info(df, company_name):
    result = df[df["Company Name"].str.contains(company_name, case=False, na=False)]
    return result.to_dict(orient="records")
