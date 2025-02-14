import clean 

def main():
  raw_data_path = "../data/raw/2016_2024.csv"
  raw_df = clean.pd.read_csv(raw_data_path)

  clean_df = clean.clean_missing_values(raw_df)
  clean_df = clean.clean_drop(clean_df)
  clean_df = clean.types_conversion(clean_df)
  clean_df = clean.impute_na(clean_df)
  clean_df = clean.reformat_values(clean_df)
  
  return raw_df, clean_df

raw_df, clean_df = main()
