# Main Hydrogen EMS Model
# Uses Germany 2019 solar and wind data as hourly profiles
# and scales them to a realistic hydrogen plant size.

import pandas as pd
from hydrogen_calculator import calculate_hydrogen


# Load cleaned Germany 2019 renewable generation data
data_path = "Data/de_generation_actual_2019_60min.csv"

df = pd.read_csv(data_path)
df["utc_timestamp"] = pd.to_datetime(df["utc_timestamp"])


# Plant renewable capacities
solar_capacity_mw = 50
wind_onshore_capacity_mw = 100
wind_offshore_capacity_mw = 0


# Electrolyzer assumptions
electrolyzer_type = "PEM"
electrolyzer_capacity_mw = 30
electrolyzer_efficiency = 0.65
operation_hours = 1


# Target capacity factors for a realistic plant
solar_capacity_factor = 0.11
wind_onshore_capacity_factor = 0.25
wind_offshore_capacity_factor = 0.40


# Create normalized profiles from Germany data
df["solar_profile"] = (
    df["de_solar_generation_actual_mw"]
    / df["de_solar_generation_actual_mw"].max()
)

df["wind_onshore_profile"] = (
    df["de_wind_onshore_generation_actual_mw"]
    / df["de_wind_onshore_generation_actual_mw"].max()
)

df["wind_offshore_profile"] = (
    df["de_wind_offshore_generation_actual_mw"]
    / df["de_wind_offshore_generation_actual_mw"].max()
)


# Adjust profiles to realistic annual capacity factors
df["plant_solar_generation_mw"] = (
    df["solar_profile"]
    * solar_capacity_mw
    * solar_capacity_factor
    / df["solar_profile"].mean()
)

df["plant_wind_onshore_generation_mw"] = (
    df["wind_onshore_profile"]
    * wind_onshore_capacity_mw
    * wind_onshore_capacity_factor
    / df["wind_onshore_profile"].mean()
)

df["plant_wind_offshore_generation_mw"] = (
    df["wind_offshore_profile"]
    * wind_offshore_capacity_mw
    * wind_offshore_capacity_factor
    / df["wind_offshore_profile"].mean()
)


# Make sure generation does not exceed installed capacity
df["plant_solar_generation_mw"] = df["plant_solar_generation_mw"].clip(
    upper=solar_capacity_mw
)

df["plant_wind_onshore_generation_mw"] = df["plant_wind_onshore_generation_mw"].clip(
    upper=wind_onshore_capacity_mw
)

df["plant_wind_offshore_generation_mw"] = df["plant_wind_offshore_generation_mw"].clip(
    upper=wind_offshore_capacity_mw
)


# Calculate total plant renewable generation
df["plant_total_renewable_generation_mw"] = (
    df["plant_solar_generation_mw"]
    + df["plant_wind_onshore_generation_mw"]
    + df["plant_wind_offshore_generation_mw"]
)

# Empty lists to store hourly results
used_power_list = []
curtailed_power_list = []
electricity_used_list = []
useful_energy_list = []
hydrogen_produced_list = []


# Run hourly hydrogen production calculation
for hour in range(len(df)):
    total_power_mw = df["plant_total_renewable_generation_mw"][hour]

    used_power_mw = min(total_power_mw, electrolyzer_capacity_mw)
    curtailed_power_mw = total_power_mw - used_power_mw

    electricity_used_mwh, useful_energy_mwh, hydrogen_produced_kg = calculate_hydrogen(
        used_power_mw,
        operation_hours,
        electrolyzer_efficiency
    )

    used_power_list.append(used_power_mw)
    curtailed_power_list.append(curtailed_power_mw)
    electricity_used_list.append(electricity_used_mwh)
    useful_energy_list.append(useful_energy_mwh)
    hydrogen_produced_list.append(hydrogen_produced_kg)


# Add hourly results to dataframe
df["used_power_mw"] = used_power_list
df["curtailed_power_mw"] = curtailed_power_list
df["electricity_used_mwh"] = electricity_used_list
df["useful_energy_mwh"] = useful_energy_list
df["hydrogen_produced_kg"] = hydrogen_produced_list


# Calculate yearly totals
total_available_energy_mwh = df["plant_total_renewable_generation_mw"].sum()
total_electricity_used_mwh = df["electricity_used_mwh"].sum()
total_curtailed_energy_mwh = df["curtailed_power_mw"].sum()
total_hydrogen_kg = df["hydrogen_produced_kg"].sum()

curtailment_percent = (
    total_curtailed_energy_mwh / total_available_energy_mwh
) * 100

electrolyzer_full_load_hours = (
    total_electricity_used_mwh / electrolyzer_capacity_mw
)


# Print results
print("Hydrogen Production from a Realistic Renewable Plant")
print("----------------------------------------------------")
print("Solar capacity:", solar_capacity_mw, "MW")
print("Onshore wind capacity:", wind_onshore_capacity_mw, "MW")
print("Offshore wind capacity:", wind_offshore_capacity_mw, "MW")
print("Electrolyzer type:", electrolyzer_type)
print("Electrolyzer capacity:", electrolyzer_capacity_mw, "MW")
print("Electrolyzer efficiency:", electrolyzer_efficiency * 100, "%")
print()

print("Annual Results")
print("--------------")
print("Total renewable energy available:", round(
    total_available_energy_mwh, 2), "MWh")
print("Total renewable energy available:", round(
    total_available_energy_mwh / 1000, 2), "GWh")
print("Total electricity used by electrolyzer:",
      round(total_electricity_used_mwh, 2), "MWh")
print("Total curtailed energy:", round(total_curtailed_energy_mwh, 2), "MWh")
print("Curtailment:", round(curtailment_percent, 2), "%")
print("Electrolyzer full-load hours:",
      round(electrolyzer_full_load_hours, 2), "h/year")
print("Total hydrogen produced:", round(total_hydrogen_kg, 2), "kg")
print("Total hydrogen produced:", round(total_hydrogen_kg / 1000, 2), "tonnes")


# Save hourly plant results
output_path = "Data/hydrogen_plant_results_2019.csv"
df.to_csv(output_path, index=False)

print()
print("Hourly results saved to:", output_path)
