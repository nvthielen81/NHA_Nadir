smaken_en_prijzen = "aarbei,3,vanille,4,choloade,5"
aanbieding =0.8
string_tmp = smaken_en_prijzen[7:8]
totaal_prijs = int(string_tmp)
totaal_prijs = totaal_prijs * aanbieding
print("Vandaag in de aanbieding: " + smaken_en_prijzen[0:6] + "ijs, 1 liter - slechts Euro " + str(totaal_prijs) + "!")

reclame_text2 = "Sportvliegtuig".upper()
print(reclame_text2)