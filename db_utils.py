import yaml
import pandas as pd
from sqlalchemy import create_engine

def load_yaml(filename):
    with open(f'{filename}','r') as f:
        credentials_dict = yaml.safe_load(f)
        credentials_list = list(credentials_dict.values())
    return(credentials_list)


class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials

    def sql_engine_connect(self):
        credentials = load_yaml('eda-project/EDA-Customer-Loans/credentials.yaml')
        engine = create_engine(f"postgresql://{credentials[2]}:{credentials[1]}@{credentials[0]}:{credentials[4]}/{credentials[3]}")
        return (engine)

    def extract_database_data(self):
        engine = self.sql_engine_connect()
        engine.connect()
        table = pd.read_sql_query('''SELECT * FROM loan_payments;''', engine)
        loan_payments = pd.DataFrame(table)
        return (loan_payments)
    
def save_to_csv():
    extracted_df = RDSDatabaseConnector('eda-project/EDA-Customer-Loans/credentials.yaml').extract_database_data()
    loan_payments_csv = extracted_df.to_csv('loan_payments.csv', index=False)
    return (loan_payments_csv)

def create_df(filname):
    df = pd.read_csv(filname)
    return(df)