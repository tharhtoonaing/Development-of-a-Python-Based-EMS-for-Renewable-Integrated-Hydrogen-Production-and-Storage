# Hourly Hydrogen Production from Renewable Power

# Hydrogen Production from Solar + Wind Power


def calculate_hydrogen(electrolyzer_power_kw, operation_hours, efficiency):
    h2_hhv_kwh_per_kg = 39.4  # kWh/kg H2

    electricity_used_kwh = electrolyzer_power_kw * operation_hours
    useful_energy_kwh = electricity_used_kwh * efficiency
    hydrogen_produced_kg = useful_energy_kwh / h2_hhv_kwh_per_kg

    return electricity_used_kwh, useful_energy_kwh, hydrogen_produced_kg


# Input data
solar_power_kw = [0, 0, 100, 300, 600, 800, 700, 400, 100, 0]
wind_power_kw = [300, 450, 500, 350, 200, 150, 400, 700, 900, 600]

operation_hours = 1

# 3. Electrolyzer data
electrolyzer_type = "PEM"
electrolyzer_capacity_kw = 700
efficiency = 0.65

total_hydrogen_kg = 0
total_electricity_kwh = 0

print("Hourly Hydrogen Production from Solar + Wind")
print("------------------------------------------------")

for hour in range(len(solar_power_kw)):
    solar_power = solar_power_kw[hour]
    wind_power = wind_power_kw[hour]
    total_power = solar_power + wind_power
    used_power = min(total_power, electrolyzer_capacity_kw)
    curtailed_power = total_power - used_power
    electricity, useful_energy, hydrogen = calculate_hydrogen(
        used_power,
        operation_hours,
        efficiency
    )

    total_hydrogen_kg += hydrogen
    total_electricity_kwh += electricity

    print("Hour:", hour,
          "| Solar:", solar_power, "kW",
          "| Wind:", wind_power, "kW",
          "| Used power:", used_power, "kW",
          "| Curtailed power:", curtailed_power, "kW",
          "| H2 produced:", round(hydrogen, 2), "kg")

print("------------------------------------------------")
print("Total electricity used:", total_electricity_kwh, "kWh")
print("Total hydrogen produced:", round(total_hydrogen_kg, 2), "kg")
