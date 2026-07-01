# Hourly Hydrogen Production from Renewable Power

def calculate_hydrogen(electrolyzer_power_kw, operation_hours, efficiency):
    h2_hhv_kwh_per_kg = 39.4  # kWh/kg H2

    electricity_used_kwh = electrolyzer_power_kw * operation_hours
    useful_energy_kwh = electricity_used_kwh * efficiency
    hydrogen_produced_kg = useful_energy_kwh / h2_hhv_kwh_per_kg

    return electricity_used_kwh, useful_energy_kwh, hydrogen_produced_kg


# Input data
renewable_power_kw = [0, 0, 100, 300, 600, 800, 700, 400, 100, 0]
efficiency = 0.75
operation_hours = 1  # each step is 1 hour

total_hydrogen_kg = 0
total_electricity_kwh = 0

print("Hourly Hydrogen Production")
print("--------------------------")

for hour, power in enumerate(renewable_power_kw):
    electricity, useful_energy, hydrogen = calculate_hydrogen(
        power, operation_hours, efficiency)

    total_hydrogen_kg += hydrogen
    total_electricity_kwh += electricity

    print("Hour:", hour,
          "| Power:", power, "kW",
          "| H2 produced:", round(hydrogen, 2), "kg")

print("--------------------------")
print("Total electricity used:", total_electricity_kwh, "kWh")
print("Total hydrogen produced:", round(total_hydrogen_kg, 2), "kg")
