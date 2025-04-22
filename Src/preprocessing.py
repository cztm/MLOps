
import pandas as pd

def load_and_preprocess_health_data(filepath):
    # Load the CSV
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.replace('?', '', regex=False)
    )

    # Drop rows where age is missing
    df = df.dropna(subset=['age'])

    # Drop the 'timestamp' column if it exists
    if 'timestamp' in df.columns:
        df.drop(columns='timestamp', inplace=True)

    return df

input_path = "data/student_mental_health.csv"
output_path = "data/cleaned_health_data.csv"

df = load_and_preprocess_health_data(input_path)
df.to_csv(output_path, index=False)

