
class Thermostat:

    def __init__(self, target_temperature, Fahrenheit_or_Celsius): #Celsius = True, Fahrenheit = False
        self._tt = target_temperature
        self._FoC = Fahrenheit_or_Celsius

    @staticmethod
    def Fahrenheit_to_Celsius(val):
        return (val - 32) * (5 / 9)

    @staticmethod
    def Celsius_to_Fahrenheit(val):
        return (val * (9 / 5)) + 32

    @classmethod
    def new_thermostat(cls, thermostat):
        return Thermostat(thermostat.target_temperature, thermostat.Fahrenheit_or_Celsius)

    @property
    def target_temperature(self):
        return self._tt

    @target_temperature.setter
    def target_temperature(self, new_val):
        if new_val > 30 and self._FoC == True:
            self._tt = 30
        elif new_val < 30 and self._FoC == True:
            self._tt = new_val
        if new_val > 86 and self._FoC == False:
            self._tt = 86
        elif new_val < 86 and self._FoC == False:
            self._tt = new_val

    @property
    def Fahrenheit_or_Celsius(self):
        return self._FoC

    @Fahrenheit_or_Celsius.setter
    def Fahrenheit_or_Celsius(self, val):
        if val == True and self._FoC != True:
            self._tt = self.Fahrenheit_to_Celsius(self._tt)
        elif val == False and self._FoC != False:
            self._tt = self.Celsius_to_Fahrenheit(self._tt)
        self._FoC = val

def main():
    termostato = Thermostat(56, True)
    print(termostato.target_temperature)
    print(termostato.Fahrenheit_or_Celsius)

    termostato.target_temperature = 50
    print(termostato.target_temperature)

    termostato.Fahrenheit_or_Celsius = False
    print(termostato.Fahrenheit_or_Celsius)
    print(termostato.target_temperature)

    termostato2 = Thermostat.new_thermostat(termostato)
    print(termostato2.target_temperature)
    print(termostato2.Fahrenheit_or_Celsius)

    termostato.Fahrenheit_or_Celsius = True
    print(termostato.target_temperature)
    print(termostato.Fahrenheit_or_Celsius)
    print(termostato2.target_temperature)
    print(termostato2.Fahrenheit_or_Celsius)

    print(Thermostat.Celsius_to_Fahrenheit(5))
    print(Thermostat.Fahrenheit_to_Celsius(41))

main()