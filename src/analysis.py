import pandas as pd
import numpy as np



# List of delay columns for reference in analysis

delay_cols = ['carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']


# Mapping of Carrier Codes to Airline Names

carrier_code_map = {
    "AA": "American Airlines",
    "F9": "Frontier Airlines",
    "B6": "JetBlue Airways",
    "OH": "PSA Airlines",              # Operates as American Eagle
    "G4": "Allegiant Air",
    "NK": "Spirit Airlines",
    "OO": "SkyWest Airlines",
    "MQ": "Envoy Air",                 # Operates as American Eagle
    "UA": "United Airlines",
    "WN": "Southwest Airlines",
    "AS": "Alaska Airlines",
    "HA": "Hawaiian Airlines",
    "DL": "Delta Air Lines",
    "9E": "Endeavor Air",               # Operates as Delta Connection
    "YX": "Republic Airways"            # Operates as American Eagle / Delta Connection / United Express
}
# Clean and preprocess the flight data for analysis

def clean_data(df):

    # Convert delay columns to numeric, coercing errors to NaN
    delay_columns = ['arr_delay', 'dep_delay', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']
    for col in delay_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Fill NaN values with 0 (assuming no delay if not specified)
    df[delay_columns] = df[delay_columns].fillna(0)
    df['cancellation_code'] = (df['cancellation_code']).astype(str)


    return df


# Create a binary column for whether the flight was delayed (arrival delay > 0 minutes)

def add_delay_indicator(df):
    df['is_delayed'] = np.where(df['arr_delay'] > 0, 1, 0)

    return df


# Create a new column for departure hour by taking the first two characters of 'crs_dep_time' and converting to integer

def add_dep_hour(df):
    df['dep_hour'] = (df['crs_dep_time'] // 100).astype(int)

    # Convert 24:00 to 00:00 for consistency
    df.loc[df['dep_hour'] == 24, 'dep_hour'] = 0 

    return df


# Analytics 


# Average delay by hour

def avg_delay_by_dep_hour (df):
    adbdh = df.groupby('dep_hour')['arr_delay'].mean()

    return adbdh
    

# Average arrival delay by carrier

def avg_arr_delay_by_carrier (df):
    aadbc = df.groupby('op_unique_carrier')['arr_delay'].mean()

    return aadbc


# Delay rate by carrier (%)

def delay_rate_pct_by_carrier (df):
    drpbc = df.groupby('op_unique_carrier')['is_delayed'].mean()*100

    return drpbc


# Total delay minutes for each type (carrier, weather, NAS, security, late aircraft)

def delay_totals_by_delay_type(df):
    dtbdt = df[delay_cols].sum()

    return dtbdt


# Total delay minutes for each type by carrier

def delay_totals_by_type_per_carrier(df):
    dtbtpc = (df.groupby('op_unique_carrier')[delay_cols].sum()).rename(index=carrier_code_map)

    return dtbtpc

# Combine key metrics into a single DataFrame for easier dashboard integration

def combine_metrics(df):
    aadbc = avg_arr_delay_by_carrier(df)
    drpbc = delay_rate_pct_by_carrier(df)
    combined = pd.DataFrame({
        'avg_arr_delay_min': aadbc.rename(index=carrier_code_map),
        'delay_rate_pct': drpbc.rename(index=carrier_code_map)
    })
    return combined

# Compute all analytics and return as dictionary for easy import
def compute_all_analytics(df):
    return {
        'avg_delay_by_dep_hour': avg_delay_by_dep_hour(df),
        'avg_arr_delay_by_carrier': avg_arr_delay_by_carrier(df),
        'delay_rate_pct_by_carrier': delay_rate_pct_by_carrier(df),
        'delay_totals_by_delay_type': delay_totals_by_delay_type(df),
        'delay_totals_by_type_per_carrier': delay_totals_by_type_per_carrier(df),   
        'combined_metrics': combine_metrics(df)
    }
