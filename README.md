# Hydrogen EMS Python Project

This project is a Python-based energy management system model for renewable hydrogen production.

The model uses Germany 2019 solar and wind generation data as hourly renewable profiles. These profiles are scaled to represent a realistic hydrogen plant instead of using the full Germany renewable generation directly.

## Current Features

* Uses Germany 2019 hourly renewable generation data
* Uses solar and onshore wind profiles
* Scales Germany generation profiles to a realistic plant size
* Applies realistic renewable capacity factors
* Calculates hourly renewable power available for the electrolyzer
* Applies electrolyzer capacity limit
* Calculates curtailed renewable energy
* Estimates hydrogen production using electrolyzer efficiency
* Saves hourly simulation results to CSV

## System Overview

Solar + Onshore Wind → PEM Electrolyzer → Hydrogen Production

At this stage, the model does not include battery storage or hydrogen storage.

## Data Source

The renewable generation data was obtained from Open Power System Data:

```text
https://data.open-power-system-data.org/weather_data/latest/
```

The model uses a cleaned Germany-only dataset:

```text
Data/de_generation_actual_2019_60min.csv
```

The original Excel file is not included because it is too large.

## Plant Assumptions

The current plant configuration is:

```text
Solar capacity: 50 MW
Onshore wind capacity: 100 MW
Offshore wind capacity: 0 MW
Electrolyzer type: PEM
Electrolyzer capacity: 30 MW
Electrolyzer efficiency: 65%
```

The renewable profiles are scaled using approximate capacity factors:

```text
Solar capacity factor: 11%
Onshore wind capacity factor: 25%
Offshore wind capacity factor: 40%
```

Offshore wind is currently set to 0 MW because the first model focuses on a realistic solar and onshore wind hydrogen plant.

## Units and Assumptions

* Power: MW
* Energy: MWh
* Hydrogen HHV: 0.0394 MWh/kg
* Time step: 1 hour
* Electrolyzer type: PEM
* Electrolyzer efficiency: 65%

## Latest Simulation Result

For the current plant configuration, the model gives:

```text
Total renewable energy available: 267,180 MWh/year
Total electricity used by electrolyzer: 248,020.71 MWh/year
Total curtailed energy: 19,159.29 MWh/year
Curtailment: 7.17%
Electrolyzer full-load hours: 8,267.36 h/year
Total hydrogen produced: 4,091.71 tonnes/year
```

This result shows that a 30 MW electrolyzer can use most of the available renewable electricity while keeping curtailment at about 7.17%.

## Project Files

```text
main.py
hydrogen_calculator.py
prepare_generation_data.py
README.md
Data/de_generation_actual_2019_60min.csv
Data/hydrogen_plant_results_2019.csv
```

## Output File

The hourly simulation results are saved to:

```text
Data/hydrogen_plant_results_2019.csv
```

This file includes hourly renewable generation, electrolyzer power use, curtailed power, electricity used, useful energy, and hydrogen production.

## Next Steps

* Compare different electrolyzer capacities
* Add hydrogen storage tank
* Add hydrogen demand profile
* Add battery storage
* Plot renewable generation, electrolyzer use, hydrogen production, and curtailment
* Analyze the best electrolyzer size based on curtailment and full-load hours
* Add optimization or machine learning later

## Purpose

The purpose of this project is to model renewable hydrogen production from realistic solar and wind profiles while considering electrolyzer efficiency, capacity limits, and curtailed energy.

* Add optimization or machine learning later

## Purpose

The purpose of this project is to model renewable hydrogen production from real solar and wind data while considering electrolyzer efficiency, capacity limits, and curtailed energy.

