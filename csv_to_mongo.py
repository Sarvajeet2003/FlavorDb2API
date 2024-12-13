import pandas as pd
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('localhost', 27017)
db = client['your_database_name']  # Replace with your database name

# List of CSV files and collections
csv_files = {
    'fdb_admet.csv': 'admet_data',
    'fdb_entities.csv': 'entities_data',
    'fdb_fn_properties.csv': 'fn_properties_data',
    'fdb_moleculeoftheday.csv': 'molecule_of_the_day_data',
    'fdb_molecules_entities.csv': 'molecules_entities_data',
    'fdb_molecules.csv': 'molecules_data',
    'fdb_more_properties.csv': 'more_properties_data',
    'fdb_receptors.csv': 'receptors_data'
}

# Function to import CSV data into MongoDB
def import_csv_to_mongodb(file_path, collection_name):
    # Load CSV data into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Convert DataFrame to dictionary and insert into MongoDB
    db[collection_name].insert_many(df.to_dict('records'))

# Iterate through all CSV files and import them
for file_name, collection_name in csv_files.items():
    file_path = f"/Users/sarvajeethuk/Desktop/BTP/flavorDB2_v1_csvs/{file_name}"  # Path to your CSV files
    import_csv_to_mongodb(file_path, collection_name)

print("Data successfully inserted into MongoDB.")
