import pandas as pd
from src.analysis import *



# Test cases for data cleaning and preprocessing functions
def test_clean_data_removes_nulls():
    df = pd.DataFrame({
        'arr_delay': ['10', '20', 'NaN', '5'],
        'dep_delay': ['5', 'NaN', '15', '0'],
        'carrier_delay': ['NaN', '0', '5', '10'],
        'weather_delay': ['0', 'NaN', '0', '5'],
        'nas_delay': ['5', '10', 'NaN', '0'],
        'security_delay': ['0', '5', '10', 'NaN'],
        'late_aircraft_delay': ['10', '0', '5', 'NaN'],
    })
    
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0  # No null values should remain

# Test cases for delay indicator function
def test_add_delay_indicator():
    df = pd.DataFrame({
        'arr_delay': [10, -5, 0]
    })
    
    df = add_delay_indicator(df)
    
    assert list(df['is_delayed']) == [1, 0, 0]

# Test cases for departure hour extraction function
def test_add_dep_hour():
    df = pd.DataFrame({
        'crs_dep_time': [500, 1200, 600, 2400, 0]
    })
    
    df = add_dep_hour(df)
    
    assert list(df['dep_hour']) == [5, 12, 6, 0, 0]