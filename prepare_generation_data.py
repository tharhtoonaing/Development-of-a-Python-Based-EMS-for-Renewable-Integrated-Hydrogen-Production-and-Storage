# Prepare Germany Renewable Generation Data
# This script extracts Germany 2019 hourly solar, wind offshore,
# and wind onshore actual generation data from the original Excel file.
# The cleaned data is saved as a smaller CSV file for the hydrogen EMS model.

import pandas as pd


def load_de_generation_data(file_path, sheet_name="60min"):
    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        skiprows=7,
        header=None,
        usecols="A,M,S,V",
        names=[
            "utc_timestamp",
            "de_solar_generation_actual_mw",
            "de_wind_offshore_generation_actual_mw",
            "de_wind_onshore_generation_actual_mw"
        ],
        engine="openpyxl"
    )

    # Convert timestamp to datetime
    df["utc_timestamp"] = pd.to_datetime(df["utc_timestamp"])

    # Replace missing values with 0
    df = df.fillna(0)

    # Calculate total wind generation from offshore and onshore wind
    df["de_total_wind_generation_actual_mw"] = (
        df["de_wind_offshore_generation_actual_mw"]
        + df["de_wind_onshore_generation_actual_mw"]
    )

    # Calculate total renewable generation from solar and wind
    df["de_total_renewable_generation_actual_mw"] = (
        df["de_solar_generation_actual_mw"]
        + df["de_total_wind_generation_actual_mw"]
    )

    return df


file_path = "Data/weather data 2020.xlsx"

df = load_de_generation_data(file_path, sheet_name="60min")

# Filter the dataframe to keep only Germany 2019 hourly data
df_2019 = df[
    (df["utc_timestamp"] >= "2019-01-01 00:00:00") &
    (df["utc_timestamp"] < "2020-01-01 00:00:00")
]

df_2019 = df_2019.reset_index(drop=True)

print(df_2019.head())
print(df_2019.tail())
print(df_2019.info())
print("Number of rows:", len(df_2019))

df_2019.to_csv("Data/de_generation_actual_2019_60min.csv", index=False)
