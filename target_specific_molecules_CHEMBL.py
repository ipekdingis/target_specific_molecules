# Import necessary libraries
import pandas as pd
from chembl_webresource_client.new_client import new_client

# Ask the user for the ChEMBL target ID
target_id = input("Enter the ChEMBL Target ID (e.g., CHEMBL1907611): ").strip()

# Query ChEMBL database for activities related to the target
activities = new_client.activity.filter(
    target_chembl_id__in=[target_id]
).only(["molecule_chembl_id", "canonical_smiles", "standard_value"])

# Check if any data was returned
if activities:
    # Convert to Pandas DataFrame
    df = pd.DataFrame(activities)

    # Rename 'standard_value' to 'IC50' for clarity
    df.rename(columns={"standard_value": "IC50"}, inplace=True)

    # Keep only the necessary columns: SMILES, molecule ID, and IC50 value
    df = df[["canonical_smiles", "molecule_chembl_id", "IC50"]]

    # Display the first few rows
    print(df.head())

    # Define the CSV filename with the target ID
    csv_filename = f"chembl_activities_{target_id}.csv"

    # Save the dataset to CSV
    df.to_csv(csv_filename, index=False)

    print(f"Data successfully saved to '{csv_filename}'")
else:
    print(f"No data found for Target ID: {target_id}")




