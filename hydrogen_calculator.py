# Hourly Hydrogen Production from Renewable Energy (Solar and Wind)


def calculate_hydrogen(electrolyzer_power_mw, operation_hours, efficiency):
    h2_hhv_mwh_per_kg = 0.0394  # mwh/kg H2

    electricity_used_mwh = electrolyzer_power_mw * operation_hours
    useful_energy_mwh = electricity_used_mwh * efficiency
    hydrogen_produced_kg = useful_energy_mwh / h2_hhv_mwh_per_kg

    return electricity_used_mwh, useful_energy_mwh, hydrogen_produced_kg
