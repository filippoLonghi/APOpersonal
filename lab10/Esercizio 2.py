
class Thermostat:

    def __init__(self, target_temperature, Fahrenheit): #Fahrenheit = True --> Fahrenheit, Fahrenheit = False --> Celsius
        self._tt = target_temperature
        self._Fahrenheit = Fahrenheit

    @classmethod
    def new_thermostat(cls, thermostat):
        return Thermostat(thermostat.target_temperature, thermostat.Fahrenheit)
            #  cls( ... )

    @staticmethod
    def Fahrenheit_to_Celsius(val):
        return (val - 32) * (5 / 9)

    @staticmethod
    def Celsius_to_Fahrenheit(val):
        return (val * (9 / 5)) + 32

    @property
    def target_temperature(self):
        return self._tt
        # if not self._Fahrenheit:
        #     return self._tt
        # else:
        #     return self.Celsius_to_Fahrenheit(self._tt)

    @target_temperature.setter
    def target_temperature(self, new_val):
        # if not self._Fahrenheit:
        #     self._tt = new_val
        # else:
        #     self._tt = self.Fahrenheit_to_Celsius(self._tt)
        #
        # if new_val > 30:
        #     self._tt = 30
        # else:
        #     self._tt = new_val

        if new_val > 30:
            self._tt = 30
        elif new_val < 30 and self._Fahrenheit == True:
            self._tt = new_val
        if new_val > 86 and self._Fahrenheit == False:
            self._tt = 86
        elif new_val < 86 and self._Fahrenheit == False:
            self._tt = new_val

    @property
    def Fahrenheit(self):
        return self._Fahrenheit

    @Fahrenheit.setter
    def Fahrenheit(self, val):
        if val == True and self._Fahrenheit != True:
            self._tt = self.Fahrenheit_to_Celsius(self._tt)
        elif val == False and self._Fahrenheit != False:
            self._tt = self.Celsius_to_Fahrenheit(self._tt)
        # self._Fahrenheit = val

# def main():
#     termostato = Thermostat(56, True)
#     print(termostato.target_temperature)
#     print(termostato.Fahrenheit)
#
#     termostato.target_temperature = 50
#     print(termostato.target_temperature)
#
#     termostato.Fahrenheit_or_Celsius = False
#     print(termostato.Fahrenheit)
#     print(termostato.target_temperature)
#
#     termostato2 = Thermostat.new_thermostat(termostato)
#     print(termostato2.target_temperature)
#     print(termostato2.Fahrenheit)
#
#     termostato.Fahrenheit_or_Celsius = True
#     print(termostato.target_temperature)
#     print(termostato.Fahrenheit)
#     print(termostato2.target_temperature)
#     print(termostato2.Fahrenheit)
#
#     print(Thermostat.Celsius_to_Fahrenheit(5))
#     print(Thermostat.Fahrenheit_to_Celsius(41))


def main():
    # metodi statici
    print("0 Celsius in Fahrenheit: {:.3f}".format(Thermostat.Celsius_to_Fahrenheit(0)))
    print("0 Fahrenheit in Celsius: {:.3f}".format(Thermostat.Fahrenheit_to_Celsius(0)))

    # metodo di classe (costruttore di copia)
    t1 = Thermostat(21.5, False)
    t2 = Thermostat.new_thermostat(t1)
    print("Target temperature: {}".format(t2.target_temperature))
    print("In Fahrenheit: {}".format(t2.Fahrenheit))

    # cambio a fahrenheit
    t1.Fahrenheit = True
    print("In Fahrenheit: {}".format(t1.Fahrenheit))
    print("Target temperature: {} Fahrenheit".format(t1.target_temperature))

    # setto temperatura in fahrenheit
    t1.target_temperature = 32
    print("Target temperature: {} Fahrenheit".format(t1.target_temperature))

    # setto temperatura in celsius sopra 30 Celsius
    t2.target_temperature = 32
    print("Target temperature: {} Fahrenheit".format(t2.target_temperature))


main()