import clean 

def main():
  raw_data_path = "../data/raw/2016_2024.csv"
  raw_df = clean.pd.read_csv(raw_data_path)

  return raw_df, clean_df

raw_df, clean_df = main()
