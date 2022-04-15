stringa1 = input("inserire la prima stringa: ").lower()
stringa2 = input("inserire la seconda stringa: ").lower()

stringa1_insieme = set()
for ch1 in stringa1:
    stringa1_insieme.add(ch1)
# stringa1_insieme = {c for c in stringa1}

stringa2_insieme = set()
for ch2 in stringa2:
    stringa2_insieme.add(ch2)
# stringa2_insieme = {c for c in stringa2}

alfabeto = "abcdefghilmnopqrstuvzjkyx"
alfabeto_inseme = set()
for let in alfabeto:
    alfabeto_inseme.add(let)
# alfabeto_insieme = {chr(65+i).lower() for i in range(26)}

caratteri_comuni = stringa1_insieme.intersection(stringa2_insieme)
caratteri_solo_in_stringa1 = stringa1_insieme.difference(stringa2_insieme)
caratteri_solo_in_stringa2 = stringa2_insieme.difference(stringa1_insieme)
tutte_le_lettere = stringa1_insieme.union(stringa2_insieme)
lettere_non_presenti = alfabeto_insieme.difference(tutte_le_lettere)

print(f'le lettere comuni sono: {caratteri_comuni}.\nI caratteri che compaiono solo nella stringa 1 sono: {caratteri_solo_in_stringa1}.\n'
      f'I caratteri che compaiono solo nella stringa 2 sono: {caratteri_solo_in_stringa2}.\nLe lettere che non compaiono in nessuna delle due stringhe sono: {lettere_non_presenti}')
