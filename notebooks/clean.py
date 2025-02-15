import pandas as pd

def clean_missing_values(data_df : pd.DataFrame)->pd.DataFrame:
    """
    Returns input DataFrame with columns having more than 20%
    of its values being missing values dropped
    """
    threshold = 0.8
    data_df = data_df.dropna(axis=1, thresh=int((1-threshold)*data_df.shape[0]))
    
    return data_df

def clean_drop(data_df : pd.DataFrame)->pd.DataFrame:
    """
    Perfroms drops of duplicated rows and unused columns
    """
    data_df = data_df.drop(["Link",
              "Source",
              "Document Type",
            ], axis=1)
    data_df.drop_duplicates(inplace = True)

    return data_df

def types_conversion(data_df : pd.DataFrame)->pd.DataFrame:
    """
    Enforces appropriate dtypes for object type columns to 
    ensure consistency
    """
    # Enforcing appropriate column datatypes
    string_cols =  data_df.select_dtypes(include=['object']).columns
    data_df.loc[:,string_cols] = data_df.loc[:,string_cols].astype("string")
        
    return data_df

def impute_na(data_df : pd.DataFrame)->pd.DataFrame:
    """
    Imputes missing values in relevant columns
    """

    data_df = data_df.fillna({"Authors with affiliations":"Unkown",
                "Authors": "Unknown",
                "Author(s) ID": "Unknown",
                "Author full names": "Unknown",
                "Author Keywords": "Unknown",
                "Affiliations": "Unknown",
                "Author Keywords":"Unknown"
              } )
    
    return data_df

def reformat_values(data_df : pd.DataFrame)->pd.DataFrame:
    """
    Reformat string values in select columns to extract meaningful 
    features for analysis
    """
    global valid_countries, authors
    
    # Extract country naems to "Countries" column
    a = data_df['Authors with affiliations'].str.extractall(r',\s([^,;]+)(?=;|$)')
    data_df["Countries"] = a.groupby(level=0).agg(', '.join)
    data_df.fillna({"Countries":"Unknown"},inplace=True)

    a = data_df["Countries"].str.split(', ').explode().value_counts()
    valid_countries = a[(a>60)].drop(["Google Research", "Microsoft Research", "IBM Research", "Microsoft", "Google","Inc.", "Intel Corporation", "Huawei Noah's Ark Lab", "Adobe Research", "Alibaba Group", "Amazon", "Google Brain", "Department of Computer Science", "Microsoft Research Asia", "SenseTime Research", "Facebook AI Research"]).index.to_list()
    valid_countries = [s.strip() for s in valid_countries]
    
    def clean_countries(country_str):
      return ", ".join([name.strip() if name.strip() in valid_countries else "Unknown" for name in country_str.split(",")])
    
    data_df["Countries"] = data_df["Countries"].apply(clean_countries)


    # Extract author names and IDs into DataFrame
    exp = r'([\w\s]+),\s*([\w\s]+)\s*\((\d+)\)'

    # Get surname, first name, and ID
    authors = data_df['Author full names'].str.extractall(exp)
    
    # Combine surname and first name into a full name
    authors['Author name'] = authors[0] + ", " + authors[1]
    
    authors = authors.rename(columns={2: "Author ID"}).drop(columns=[0, 1]).reset_index(drop=True)
    authors.loc[:,"Author ID"] = pd.to_numeric(authors["Author ID"])

    return data_df