# Hydrogen Production Calculator with Efficiency

def calculate_hydrogen(electrolyzer_power_kw, operation_hours, efficiency):
    h2_hhv_kwh_per_kg = 39.4  # kWh/kg H2

    electricity_used_kwh = electrolyzer_power_kw * operation_hours
    useful_energy_kwh = electricity_used_kwh * efficiency
    hydrogen_produced_kg = useful_energy_kwh / h2_hhv_kwh_per_kg

    return electricity_used_kwh, useful_energy_kwh, hydrogen_produced_kg


# Input values
power_kw = 1000
hours = 5
efficiency = 0.75

# Run calculation
electricity, useful_energy, hydrogen = calculate_hydrogen(
    power_kw, hours, efficiency)

# Output
print("Hydrogen Production Calculator")
print("------------------------------")
print("Electrolyzer power:", power_kw, "kW")
print("Operation time:", hours, "hours")
print("Efficiency:", efficiency * 100, "%")
print("Electricity used:", electricity, "kWh")
print("Useful hydrogen energy:", useful_energy, "kWh")
print("Hydrogen produced:", round(hydrogen, 2), "kg")
