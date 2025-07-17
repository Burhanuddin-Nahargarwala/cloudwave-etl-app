import pandas as pd

# This is a sample of the data our script processes
SAMPLE_DATA = [{
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    'company': {'name': 'Romaguera-Crona'}
}]

def test_column_transformation():
    """Unit test to ensure columns are renamed and added correctly."""
    df = pd.DataFrame(SAMPLE_DATA)
    
    # Replicating the transformation logic from the script
    transformed_df = df[['id', 'name', 'username', 'email', 'company']]
    transformed_df = transformed_df.rename(columns={'id': 'user_id', 'name': 'full_name'})
    transformed_df['company_name'] = transformed_df['company'].apply(lambda c: c['name'])
    
    # Check if the columns exist
    assert 'user_id' in transformed_df.columns
    assert 'full_name' in transformed_df.columns
    assert 'company_name' in transformed_df.columns
    # Check if the old columns are gone
    assert 'id' not in transformed_df.columns
    assert 'name' not in transformed_df.columns