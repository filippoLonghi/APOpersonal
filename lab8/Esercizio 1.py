class Room:

    def __init__(self, sm, windows, power_outlets):
        self._sm = sm
        self._windows = windows
        self._power_outlets = power_outlets

    def get_sm(self):
        return self._sm

    def get_windows(self):
        return self._windows

    def get_power_outlets(self):
        return self._power_outlets

class BathRoom(Room):

    def __init__(self, sm, windows, power_outlets, sinks, showers, bath_tub, bidet):
        super().__init__(sm, windows, power_outlets)
        self._sinks = sinks
        self._showers = showers
        self._bath_tub = bath_tub
        self._bidet = bidet

    def get_sinks(self):
        return self._sinks

    def get_showers(self):
        return self._showers

    def get_bath_tub(self):
        return self._bath_tub

    def get_bidet(self):
        return self._bidet
#
# def main():
#     stanza = Room(120, 10, 25)
#     bagno = BathRoom(120, 10, 25, 2, True, True, False)
#
#     print(bagno.get_sinks())
#     print(bagno.get_showers())
#     print(bagno.get_bath_tub())
#     print(bagno.get_bidet())
#
#     print(bagno.get_sm())
#     print(bagno.get_windows())
#     print(bagno.get_power_outlets())

def main():
    # questo esempio mostra come classe figlio eredita metodo classe padre
    r1 = Room(15, 2, 5)
    r2 = BathRoom(8, 1, 3, 2, False, True, True)

    print("Room square meters: {}".format(r1.get_sm()))
    print("BathRoom square meters: {}".format(r2.get_sm()))

    print("Room windows: {}".format(r1.get_windows()))
    print("BathRoom windows: {}".format(r2.get_windows()))

    print("Room outlets: {}".format(r1.get_power_outlets()))
    print("BathRoom outlets: {}".format(r2.get_power_outlets()))

    print("BathRoom sinks: {}".format(r2.get_sinks()))
    print("BathRoom shower: {}".format(r2.get_showers()))
    print("BathRoom tub: {}".format(r2.get_bath_tub()))
    print("BathRoom bidet: {}".format(r2.get_bidet()))

    print("r2 is instance of Room: {}".format(isinstance(r2, Room)))
    print("r1 is instance of BathRoom: {}".format(isinstance(r1, BathRoom)))
    print("r2 is instance of BathRoom: {}".format(isinstance(r2, BathRoom)))


main()
