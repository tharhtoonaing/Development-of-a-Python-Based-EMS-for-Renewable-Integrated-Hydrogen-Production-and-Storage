# Hourly Hydrogen Production from Renewable Energy (Solar and Wind)

import pandas as pd


def calculate_hydrogen(electrolyzer_power_mw, operation_hours, efficiency):
    h2_hhv_mwh_per_kg = 0.0394  # mwh/kg H2

    electricity_used_mwh = electrolyzer_power_mw * operation_hours
    useful_energy_mwh = electricity_used_mwh * efficiency
    hydrogen_produced_kg = useful_energy_mwh / h2_hhv_mwh_per_kg

    return electricity_used_mwh, useful_energy_mwh, hydrogen_produced_kg


# Input data
solar_power_mw = [0, 0, 100, 300, 600, 800, 700, 400, 100, 0]
wind_power_mw = [300, 450, 500, 350, 200, 150, 400, 700, 900, 600]

operation_hours = 1

# 3. Electrolyzer data
electrolyzer_type = "PEM"
electrolyzer_capacity_mw = 1000
efficiency = 0.65

total_hydrogen_kg = 0
total_electricity_mwh = 0

print("Hourly Hydrogen Production from Solar + Wind")
print("------------------------------------------------")

for hour in range(len(solar_power_mw)):
    solar_power = solar_power_mw[hour]
    wind_power = wind_power_mw[hour]
    total_power = solar_power + wind_power
    used_power = min(total_power, electrolyzer_capacity_mw)
    curtailed_power = total_power - used_power
    electricity, useful_energy, hydrogen = calculate_hydrogen(
        used_power,
        operation_hours,
        efficiency
    )

    total_hydrogen_kg += hydrogen
    total_electricity_mwh += electricity

    print("Hour:", hour,
          "| Solar:", solar_power, "mw",
          "| Wind:", wind_power, "mw",
          "| Used power:", used_power, "mw",
          "| Curtailed power:", curtailed_power, "mw",
          "| H2 produced:", round(hydrogen, 2), "kg")

print("------------------------------------------------")
print("Total electricity used:", total_electricity_mwh, "mwh")
print("Total hydrogen produced:", round(total_hydrogen_kg, 2), "kg")
