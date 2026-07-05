# Hydrogen EMS Python Project

This project is a beginner-friendly Python model for renewable hydrogen production. It calculates hydrogen production from solar and wind power using an electrolyzer.

## Current Features

* Calculates hydrogen production from electrolyzer power, operating time, and efficiency
* Uses HHV of hydrogen as the energy basis
* Includes hourly solar power input
* Includes hourly wind power input
* Combines solar and wind power
* Adds electrolyzer capacity limit
* Calculates curtailed renewable power when available power is higher than electrolyzer capacity

## Current System

Solar Power + Wind Power → Electrolyzer → Hydrogen Production

At the current stage, the system does not include a battery or hydrogen storage tank yet.

## Assumptions

* Electrolyzer type: PEM
* Electrolyzer capacity: 700 kW
* Electrolyzer efficiency: 65%
* Hydrogen HHV: 39.4 kWh/kg
* Time step: 1 hour

## Example Calculation Logic

The model first calculates total renewable power:

```python
total_power = solar_power + wind_power
```

Then it limits the power based on electrolyzer capacity:

```python
used_power = min(total_power, electrolyzer_capacity_kw)
```

Curtailed power is calculated as:

```python
curtailed_power = total_power - used_power
```

Hydrogen production is then calculated using:

```python
hydrogen_produced_kg = useful_energy_kwh / h2_hhv_kwh_per_kg
```

## Next Steps

* Add hydrogen storage tank
* Add hydrogen demand
* Track hydrogen storage level hour by hour
* Add plots using matplotlib
* Add CSV input data using pandas
* Compare PEM and alkaline electrolyzer operation
* Later add machine learning or optimization features

## Purpose

The purpose of this project is to develop a Python-based model for renewable hydrogen production and energy management. The project focuses on simulating hydrogen production from solar and wind power, considering electrolyzer efficiency, capacity limits, and curtailed renewable energy. It will be gradually expanded with hydrogen storage, demand profiles, data analysis, and optimization features.
