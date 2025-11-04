
wiek_studenta_1=input("wiek pierwszego studenta:")
wiek_studenta_2=input("wiek drugiego studenta:") 

print (wiek_studenta_1)
print (wiek_studenta_2)

wiek_studenta_1= int(wiek_studenta_1)
wiek_studenta_2 = int(wiek_studenta_1)

if (wiek_studenta_1 > wiek_studenta_2):
    tekst = "Pierwszy student jest starszy i ma"+(wiek_studenta_1)+"lat(a)"
    print(tekst)

with open("wiek.txt","a")as plik:
    plik.write(tekst)2

