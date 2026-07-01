# Garden Guardian: Data Engineering for Smart Agriculture

This project focuses on building resilient data pipelines for smart agricultural and IoT digital greenhouse systems. You will master Python's exception handling structures (try/except/finally/raise) to manage sensor failures and process agricultural data streams gracefully.

## General Instructions
* Python Version: Python 3.10+
* Linter: Code must respect flake8 standards
* Type Hinting: Include explicit type hints verified via mypy
* Stability: Programs must never crash

## Repository Structure
* ex0/ft_first_exception.py
* ex1/ft_raise_exception.py
* ex2/ft_different_errors.py
* ex3/ft_custom_errors.py
* ex4/ft_finally_block.py

## Exercise Summary

### Exercise 0: Agricultural Data Validation
Safely parse raw field sensor string data into integer format using an input_temperature(temp_str) function. Intercept bad user inputs or corrupted transmissions without crashing the execution loop.

### Exercise 1: Agricultural Data Validation Pipeline
Expand the validation pipeline to evaluate logic boundaries. Explicitly raise an error if a valid numeric temperature drops below 0°C or exceeds 40°C, rendering it unsafe for crops.

### Exercise 2: Different Types of Problems
Isolate and map diverse exceptions within a garden_operations function. Trap ValueError, ZeroDivisionError, FileNotFoundError, and TypeError conditions separately to demonstrate structural monitoring.

### Exercise 3: Making Your Own Error Types
Construct custom error hierarchies to replace generic built-in Python messages with clear domain context. Introduces inheritance logic: GardenError -> PlantError & WaterError.

### Exercise 4: Finally Block - Always Clean Up
Use the structural guarantee of a finally block to execute system cleanup. Ensure open irrigation channels or active hardware pathways close safely even if a runtime plant exception forces an early return.
