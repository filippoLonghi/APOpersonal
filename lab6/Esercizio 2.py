class Id:
    _numero_documento = 0
    def __init__(self, nome, cognome, anno_rilascio=2022):
        self._nome = nome
        self._cognome = cognome
        self._anno_rilascio = anno_rilascio
        self._anno_nascita = "non disponibile" #None
        Id._numero_documento += 1
        # self._numero_documento = Id._numero_documento

    def get_cognome(self):
        return self._cognome

    def get_nome(self):
        return self._nome

    def get_anno_rilascio(self):
        return self._anno_rilascio

    def set_birth_year(self, anno_nascita):
        if anno_nascita >= self._anno_rilascio:
            self._anno_nascita = self._anno_rilascio
        else:
            self._anno_nascita = anno_nascita

    def get_anno_nascita(self):
        return self._anno_nascita

    def get_numero_documento(self):
        return Id._numero_documento #self._numero_documento

def main():
    prima_carta_identità = Id("Mario", "Rossi")
    prima_carta_identità.set_birth_year(2025)
    print(prima_carta_identità.get_anno_nascita()) #anno_nascita = anno_rilascio --> 2022)
    print(prima_carta_identità.get_anno_rilascio()) #anno_rialscio impostato come default --> 2022
    print(prima_carta_identità.get_numero_documento()) #ho registrato il primo documento --> 1

    seconda_carta_identità = Id("Mario", "Rossi", 2034)
    seconda_carta_identità.set_birth_year(2003)
    print(seconda_carta_identità.get_anno_nascita()) # --> 2003
    print(seconda_carta_identità.get_anno_rilascio()) #--> 2034
    print(seconda_carta_identità.get_numero_documento()) #è indifferente chiamare il getter sul primo o secodno documento, il contatore si è già incrementato --> 2

main()
