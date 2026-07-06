# Hydrogen EMS Python Project

This project is a Python-based model for renewable hydrogen production using real solar and wind generation data from Germany.

## Current Features

* Uses Germany 2019 hourly renewable generation data
* Includes solar, offshore wind, and onshore wind actual generation
* Calculates total renewable power
* Applies electrolyzer capacity limit
* Calculates curtailed renewable power
* Estimates hydrogen production using electrolyzer efficiency

## System Overview

Solar + Offshore Wind + Onshore Wind → Electrolyzer → Hydrogen Production

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

## Units and Assumptions

* Power: MW
* Energy: MWh
* Hydrogen HHV: 0.0394 MWh/kg
* Time step: 1 hour
* Electrolyzer type: PEM
* Electrolyzer efficiency: 65%

## Project Files

```text
main.py
hydrogen_calculator.py
prepare_generation_data.py
README.md
Data/de_generation_actual_2019_60min.csv
```

## Next Steps

* Add hydrogen storage tank
* Add hydrogen demand
* Add plots with matplotlib
* Compare electrolyzer capacities
* Analyze curtailed energy
* Add optimization or machine learning later

## Purpose

The purpose of this project is to model renewable hydrogen production from real solar and wind data while considering electrolyzer efficiency, capacity limits, and curtailed energy.

* Add optimization or machine learning later

## Purpose

The purpose of this project is to model renewable hydrogen production from real solar and wind data while considering electrolyzer efficiency, capacity limits, and curtailed energy.

