
from thermostat_utils import run_thermostat
from thermostats import PIThermostat, PIHeatingThermostat


# This function controls temperature in your room...
# Let's see how it works!
class LocalThermostat:
    def __init__(self, target):
        self.target = target

    def __call__(self, current_temperature: float) -> float:
        if current_temperature < self.target:
            return 1.0
        return 0.0


thermostat = LocalThermostat(25)

run_thermostat(thermostat, 30)

# Tasks:
# 0. Why is that code making "sawtooth" signal? How much does the temperature change?
# 1. Change the initial room temperature to something above temperature that you'd like to have:
#   a) what do you observe?
#   b) how to fix the situation?
#   c) what is needed to cool a room?
# 2. Turning heating on & off all the time can break heater, how to heat more and then make it cool down longer:
#   a) HINT #1: check term: hysteresis
#   b) HINT #2: you need extra state to make it work
# 3. Sometimes you need to keep the temperature constant, how to do it?
#   a) HINT #1: proportional controller,
#   b) Did you reach the set-point? Try using PI controller








