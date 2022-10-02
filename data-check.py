# DATA CHECKS
import pandas as po
import sys
def check_month_year_label(df : po.DataFrame):
    """
    Checking that dates are correct between the three columns
    """
    for i, row in df.iterrows():
        month = row['Time.Month']
        year = row['Time.Year']

        assert month == row['Time.Label'].month, "Mismatch between Time.Label and Time.Month columns at index {}".format(row.index)
        assert year == row['Time.Label'].year, "Mismatch between Time.Label and Time.Year columns at index {}".format(row.index)
    return
 
def check_airport_name_code_uniqueness(df : po.DataFrame):
    """
    Checking that each Airport Name is uniquely identified by its Airport Code
    """
    num_names = df['Airport.Name'].unique().shape[0]
    num_codes = df['Airport.Code'].unique().shape[0]
    assert num_names == num_codes, "Airport.Name: {} unique values, Airport.Code: {} unique values".format(num_unique_names, num_unique_codes)
    assert all(df.groupby('Airport.Name').agg(lambda g: len(g.unique()))['Airport.Code'] == 1), "Airport.Name not 1-1 with Airport.Code"
    return
 
def check_carrier_list_length(df : po.DataFrame):
    """
    Checking that the number of carrier names is consistent with the provided list of carrier names
    """
    assert (all(df['Statistics.Carriers.Names'].str.split(',').apply(lambda row: len(row)) == df['Statistics.Carriers.Total']), 
            "Mismatch between length of Statistics.Carriers.Names and Statistics.Carriers.Total columns")
    return

def check_nonnegative_values(df : po.DataFrame):
    pass

if __name__ == "__main__":
    data = sys.argv[1]
    print(data)
    check_month_year_label(data)
    check_airport_name_code_uniqueness(data)
    check_carrier_list_length(data)
    check_nonnegative_values(data)
    print("Everything passed")