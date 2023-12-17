class Thermostat:
    def __init__(self, target):
        self.target = target

    def __call__(self, current_temperature):
        if current_temperature < self.target:
            return 1.0
        if current_temperature > self.target:
            return -1.0
        return 0.0


class HeatingThermostat:
    def __init__(self, target):
        self.target = target

    def __call__(self, current_temperature):
        if current_temperature < self.target:
            return 1.0


class HeatingThermostatWithHysteresis:
    def __init__(self, target, hysteresis=2):
        self.target = target
        self.hysteresis = hysteresis
        self.heating = True

    def __call__(self, current_temperature):
        if current_temperature < self.target - self.hysteresis:
            self.heating = True
        if current_temperature > self.target + self.hysteresis:
            self.heating = False

        return 1.0 if self.heating else 0.0


class HeatingAndCoolingThermostat:
    def __init__(self, target, hysteresis = 2):
        self.target = target
        self.hysteresis = hysteresis
        self.heating = True
        self.cooling = False

    def __call__(self, current_temperature):
        if current_temperature > self.target + self.hysteresis:
            self.cooling = True
            self.heating = False
        elif current_temperature < self.target + self.hysteresis:
            self.cooling = False
            self.heating = True
        else:
            self.heating = False
            self.cooling = False

        if self.heating:
            return 1.0
        if self.cooling:
            return -1.0

        return 0.0


class ProportionalThermostat:
    def __init__(self, target):
        self.target = target

    def __call__(self, current_temperature):
        delta = (self.target - current_temperature) * 0.1
        delta = max(delta, -1.0)
        delta = min(delta, 1.0)
        return delta


class PIThermostat:
    def __init__(self, target, i_coeff = 0.5):
        self.target = target
        self.delta_sum = 0.0
        self.i_coeff = i_coeff

    def __call__(self, current_temperature):
        delta = (self.target - current_temperature) * 0.1
        delta = max(delta, -1.0)
        delta = min(delta, 1.0)
        self.delta_sum += delta
        return delta + self.delta_sum * self.i_coeff


class PIHeatingThermostat:
    def __init__(self, target, i_coeff = 0.5):
        self.target = target
        self.delta_sum = 0.0
        self.i_coeff = i_coeff

    def __call__(self, current_temperature):
        delta = (self.target - current_temperature) * 0.1
        delta = max(delta, -1.0)
        delta = min(delta, 1.0)
        self.delta_sum += delta
        return max(delta + self.delta_sum * self.i_coeff, 0.0)