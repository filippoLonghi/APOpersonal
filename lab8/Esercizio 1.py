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

def main():
    stanza = Room(120, 10, 25)
    bagno = BathRoom(120, 10, 25, 2, True, True, False)

    print(bagno.get_sinks())
    print(bagno.get_showers())
    print(bagno.get_bath_tub())
    print(bagno.get_bidet())

    print(bagno.get_sm())
    print(bagno.get_windows())
    print(bagno.get_power_outlets())

main()
