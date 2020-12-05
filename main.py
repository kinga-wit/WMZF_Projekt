print(“Symulacja ruchu ciał niebieskich z wykorzystaniem Praw Keplera”)     
print(“Kinga Witschenbach”)
print(“Wiktoria Czechońska”)

# w wstępie 
#ewentualne ciekawostki co do ciał niebieskich i Keplera

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
        print ("")
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
