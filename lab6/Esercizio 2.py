class Id:
    numero_documento = 0
    def __init__(self, nome, cognome, anno_rilascio=2022):
        self.nome = nome
        self.cognome = cognome
        self.anno_rilascio = anno_rilascio
        self.anno_nascita = "non disponibile"
        Id.numero_documento += 1

    def get_cognome(self):
        return self.nome

    def get_nome(self):
        return self.cognome

    def get_anno_rilascio(self):
        return self.anno_rilascio

    def set_birth_year(self, anno_nascita):
        if anno_nascita > self.anno_rilascio:
            self.anno_nascita = self.anno_rilascio
        else:
            self.anno_nascita = anno_nascita

    def get_anno_nascita(self):
        return self.anno_nascita

    def get_numero_documento(self):
        return Id.numero_documento

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
    print(prima_carta_identità.get_numero_documento()) #è indifferente chiamare il getter sul primo o secodno documento, il contatore si è già incrementato --> 2

main()
