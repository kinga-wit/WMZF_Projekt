print(“Symulacja ruchu ciał niebieskich z wykorzystaniem Praw Keplera”)     
print(“Kinga Witschenbach”)
print(“Wiktoria Czechońska”)

# w wstępie 
#ewentualne ciekawostki co do ciał niebieskich i Keplera

cialaniebieskie = ("Ciało niebieskie \n każdy naturalny obiekt fizyczny oraz układ powiązanych ze sobą obiektów lub ich struktur, występujący w przestrzeni kosmicznej poza granicą atmosfery ziemskiej.\n Ciała niebieskie są przedmiotem zainteresowania astronomii.\n Wśród ciał niebieskich wyróżnia się obiekty, układy i struktury.\n Hipotetyczne ciało niebieskie rozmiarów planety to obiekt synestialny.")
johanneskepler = ("Johannes Kepler – niemiecki matematyk, astronom i astrolog, jedna z czołowych postaci rewolucji naukowej w XVII wieku.\n Najbardziej znany jest z nazwanych jego nazwiskiem praw ruchu planet, skodyfikowanych przez późniejszych astronomów na podstawie jego prac Astronomia nova, Harmonices Mundi i Epitome astronomiae Copernicanae.\n Prawa te wykorzystano do potwierdzenia słuszności teorii grawitacji Isaaca Newtona.")
ciekawostka1 =("Światło dochodzi w 8 minut ze Słońca do Ziemi.\n")
ciekawostka2 =("Na Wenus zamiast opadów śniegu, są opady metalu.")
numery=[]
print("Jeśli chcesz dowiedzieć się kim był Joannes Kepler wybierz 1")
print("Jeśli chcesz dowiedzieć się co to ciała niebieskie wybierz 2")
print("Jeśli chcesz zobczyć ciekawostki wybierz 3")
print("Jeśli chcesz zakończyć należy wpisać 0")

while numery != 0 :
    numery = int(input("\nWybierz o czym chcesz się dowiedzieć : "))

    if (numery == 1 ):
        print (cialaniebieskie)
    elif (numery == 2 ):
        print (johanneskepler)
    elif (numery == 3 ):
        print(ciekawostka1,ciekawostka2)
    elif (numery == 0 ):
        break
    else :
        print("Błąd")

print ("KONIEC")

#napisany kod co do praw keplera ich treści z wyborem przez użytkownika
#do wyboru 1 2 3 lub zakończ 

prawo1 = ("Każda planeta Układu Słonecznego porusza się wokół Słońca po orbicie w kształcie elipsy, w której w jednym z ognisk jest Słońce.")
prawo2 = ("W równych odstępach czasu promień wodzący planety, poprowadzony od Słońca, zakreśla równe pola.")
prawo3 = ("Stosunek kwadratu okresu obiegu planety wokół Słońca do sześcianu wielkiej półosi jej orbity jest stały dla wszystkich planet w Układzie Słonecznym")

numery=[]
print ("Jeśli Chcesz zobaczyć jedno z praw trzeba wpisać numer (1,2,3) jeśli chcesz zakończyć należy wpisać 0 ")
while numery != 0 :
    numery = int(input("Wybierz które prawo chcesz zobczyć: "))

    if (numery == 1 ):
        print (prawo1)
    elif (numery == 2 ):
        print (prawo2)
    elif (numery == 3 ):
        print (prawo3)
    elif (numery == 0):
        break
    else :
        print("Błąd")

print ("KONIEC")

#zaimportowany plik z danymi planet 
#możliwość obliczeń ich w wzorach przez użytkownika 

#przedstawienie ruchu planet wokół słońca
#ewentualny wykres

#przedstawienie symulacji ruchu ciał na wykresie 

#jako dodatek do programu gra o temacie astronomii

# Ewentualny dodatkowy program...

#ciekawe zakończenie programu 
