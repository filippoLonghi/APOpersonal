stringa1 = input("inserire la prima stringa: ")
stringa2 = input("inserire la seconda stringa: ")

stringa1_insieme = set()
stringa2_insieme = set()
alfabeto = "abcdefghilmnopqrstuvzjkyx"
alfabeto_inseme = set()

for ch1 in stringa1:
    stringa1_insieme.add(ch1)
for ch2 in stringa2:
    stringa2_insieme.add(ch2)
for let in alfabeto:
    alfabeto_inseme.add(let)

caratteri_comuni = stringa1_insieme.intersection(stringa2_insieme)
caratteri_solo_in_stringa1 = stringa1_insieme.difference(stringa2_insieme)
caratteri_solo_in_stringa2 = stringa2_insieme.difference(stringa1_insieme)
tutte_le_lettere = stringa1_insieme.union(stringa2_insieme)
lettere_non_presenti = alfabeto_inseme.difference(tutte_le_lettere)

print(f'le lettere comuni sono: {caratteri_comuni}.\nI caratteri che compaiono solo nella stringa 1 sono: {caratteri_solo_in_stringa1}.\n'
      f'I caratteri che compaiono solo nella stringa 2 sono: {caratteri_solo_in_stringa2}.\nLe lettere che non compaiono in nessuna delle due stringhe sono: {lettere_non_presenti}')
