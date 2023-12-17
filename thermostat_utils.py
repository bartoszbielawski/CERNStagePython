import time
from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class TemperatureControlDevice:
    can_heat: bool
    can_cool: bool

    def process(self, delta):
        if not self.can_heat and delta > 0:
            delta = 0
        if not self.can_cool and delta < 0:
            delta = 0
        return delta

class Room:
    def __init__(self, environment_temperature, tcd: TemperatureControlDevice, coeff: float = 0.1):
        self.environment_temperature = environment_temperature
        self.temperature = environment_temperature
        self.temperature_control_device = tcd
        self.coeff = coeff
        self.temperature_history = []

    def tick(self, temperature_delta):
        temperature_delta = min(max(temperature_delta, -1.0), 1.0)
        self.temperature += self.temperature_control_device.process(temperature_delta)
        self.temperature -= (self.temperature - self.environment_temperature) * self.coeff
        self.temperature_history.append(self.temperature)




def update_plot(fig, data):
    fig.clear()
    ax = fig.subplots()
    ax.plot(data)
    plt.pause(0.1)

def run_thermostat(thermostat, initial_room_temperature: float):
    room = Room(initial_room_temperature, TemperatureControlDevice(True, True), 0.01)

    temp_fig = plt.figure()
    plt.ion()

    while True:
        r = thermostat(room.temperature)
        if r is None:
            r = 0.0
        room.tick(r)
        print(f"{room.temperature:.2f}")
        update_plot(temp_fig, room.temperature_history)






