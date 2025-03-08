from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import yaml


def load_yaml(filename):
    """
    This method reads yaml file to return credentials details
    
    The method passes the filename as a parameter. It is used to read the credentials.yaml file and returns the
    values in a list.
    """
    with open(f'{filename}','r') as f:
        credentials_dict = yaml.safe_load(f)
        credentials_list = list(credentials_dict.values())
    return(credentials_list)


class RDSDatabaseConnector:
    """
    Attributes:
        credentials: credential details to connect with SQL engine
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def sql_engine_connect(self):
        """
        This method initialises a SQLAlchemy engine. 
        
        The method uses the load_yaml function and passes the credentials.yaml file to return it's values in 
        a list. The list values are indexed to insert the correct details in the create_engine function to 
        create an engine. 
        """
        credentials = load_yaml('credentials.yaml')
        engine = create_engine(f"postgresql://{credentials[2]}:{credentials[1]}@{credentials[0]}:{credentials[4]}/{credentials[3]}")
        return (engine)

    def extract_database_data(self):
        """
        This method returns a dataframe from the loan_payments table in the database.

        The engine from the sql_engine_connect function is returned and used to establish a connecttion. 
        Pandas read_sql_query function is used to return all colunms from the loan_payments table, which 
        creates a dataframe. 
        """
        engine = self.sql_engine_connect()
        engine.connect()
        loan_payments = pd.read_sql_query('''SELECT * FROM loan_payments;''', engine)
        return (loan_payments)
    
def save_to_csv():
    """
    This function saves the database data in the csv format. 

    The extract_database_data method from the RDSDatabaseConnector class is called, taking in the
    credentials.yaml file to return the loan_payments dataframe. The .csv funciton is used to save
    the database as a csv file to speed up loading up the data when performing analytics. 
    """
    extracted_df = RDSDatabaseConnector('credentials.yaml').extract_database_data()
    loan_payments_csv = extracted_df.to_csv('loan_payments.csv', index=False)
    return (loan_payments_csv)

def create_df():
    """
    This function creates a Pandas dataframe from the csv file. 

    The funtion runs the save_to_csv function to access the csv file. It uses the Pandas read_csv function to read the file and
    return it as a dataframe. Also, the set_option funciton is used to show all columns when the dataframe is displayed.  
    """
    save_to_csv()
    df = pd.read_csv('loan_payments.csv')
    return(df)

if __name__ == '__main__':
    save_to_csv()