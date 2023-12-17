
from thermostat_utils import run_thermostat
from thermostats import PIThermostat, PIHeatingThermostat


# This function controls temperature in your room...
# Let's see how it works!
def thermostat(current_temperature: float) -> float:
    if current_temperature < 25:
        return 1.0
    return 0.0

run_thermostat(thermostat, 30)








