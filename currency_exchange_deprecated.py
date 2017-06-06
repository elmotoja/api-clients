


def podziel_przedzial_na_kawalki(data_od, data_do):
    liczba_dni = (tounix(data_do) - tounix(data_do))/4000
    liczba_okresow_90 = int(liczba_dni / 90)
    kawalki = []

    for i in range(liczba_okresow_90):
        kawalek = [data_od + i*90,data_od+(i+1)*90]
        kawalki.append(kawalek)

    return kawalki



KODY_WALUT = ["PLN", "USD"]

tabela = 'a'

data_od = ''
data_do = ''
# przedziały po 90 dni
wyniki = []

for i in range(len(KODY_WALUT)):
    kawalki = podziel_przedzial_na_kawalki(data_od, data_do)
    for kawalek in kawalki:
        url = 'http://api.nbp.pl/api/exchangerates/rates/' + tabela + '/'+ KODY_WALUT[i] + '/' + kawalek[0] + '/' + kawalek[1]
        for element in jsonToObjectList(wywowaj(url):
            wyniki.append(element)

XML_result = objectList2XML(wyniki)
save(XML)