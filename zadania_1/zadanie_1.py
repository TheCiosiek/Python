import math
age = int (input ('Ile masz lat?\n'))
while age<=0:
    print("Wpisano nieprawidłowy wiek, wprowadź wartość jeszcze raz")
    age = int (input())
if (age>=18):
    print("Jesteś pełnoletni/-a")
else:
    print("Nie masz ukończonych 18 lat")
print ("--------kolejny program--------\n")
age = int (input ('Ile masz lat?\n'))
while age<=0:
    print("Wpisano nieprawidłowy wiek, wprowadź wartość jeszcze raz")
    age = int (input())
#tak naprawde można byłoby zostawić tylko jedną funkcje input 
if age>=18:
    print("Możesz prowadzić samochód oraz głosować w wyborach.")
elif age>=16:
    print("„Możesz prowadzić samochód.")
elif age>0:
    print("Nie możesz głosować ani prowadzić samochodu.")
else:
    print("Wprowadz prawidłowy wiek.")
print("--------kolejny program--------\n")

speed = int (input ('Z miejscowości A do B jest 250 km i 2 godzin 45 minuty jazdy pociągiem.\nWprowadź liczbe w km/h z jaką średnią predkoscią byś jechał,\nja dla Ciebie obliczę czy szybciej dotrzesz samochodem, czy pociągiem.\n'))
while speed<=0:
    print("Wpisano nieprawidłową prędkość, wprowadź wartość jeszcze raz")
    speed = int (input())
time=250/speed
hours = math.trunc(time)
minutes=60*(time-hours)
minutes=round (minutes)
print (f"Bedziesz jechał {hours} godzin i {minutes} minut. ",end='')
if time>2.75:
    print("Szybciej dojedziesz pociągiem.")
elif time==2.75:
    print("Będziesz jechał tyle samo samochodem i pociągiem.")
else:
    print("Szybciej dojedziesz samochodem.")
print("--------kolejny program--------\n")
print("Wpisz podane wartości, a ja dla Ciebie oblicze jaki będzie zwrot z inwestycji\nzakładając, że z każdego miesiąca będziesz miał 2% zysku.")
capital = int (input("Wprowadź kapitał początkowy:"))
income = int (input("Wprowadź miesięczne wpływy: "))
time_investing = int (input("Wprowadź okres inwestowania: "))
desired_cash = int (input("Wprowadź pożądaną kwotę końcową: "))
while capital<0 or income<0 or time_investing<0 or desired_cash<0:
    print("Wprowadzono nieprawidłową wartość, wprowadź wartości jeszcze raz.")
    capital = int (input("Wprowadź kapitał początkowy: "))
    income = int (input("Wprowadź miesięczne wpływy: "))
    time_investing = int (input("Wprowadź okres inwestowania: "))
    desired_cash = int (input("Wprowadź pożądaną kwotę końcową: "))
for i in range(0, time_investing):
    if i==0:
        end_capital = capital*1.02
    else:
        end_capital= (end_capital + income)*1.02
end_capital = round(end_capital, 2)
print(f"Twój końcowy kapitał to {end_capital} i ", end='')
if desired_cash<end_capital:
    print("inwestycja przewyższa twoje oczekiwania.")
elif desired_cash==end_capital:
    print("inwestycja inwestycja jest równa twoim oczekiwaniom")
else:
   print("inwestycja jest mniejsza niż twoje oczekiwania.") 
print("--------kolejny program--------\n")
run_next=1
while(run_next==1):
        print("Wprowadź dwie liczby, a ja dla Ciebie znajdę ich najmniejszą wspólną wielokrotność")
        x = float (input("Liczba x:"))
        y = float (input("Liczba y:"))
        i=1
        while(True):
                z=x*i
                if z%y==0:
                    print(f"Najmniejsza wspólna wielokrotność twoich liczb to: {z}")
                    break
                i=i+1
        run_next=int(input("--------------------------------------------------------------------------\nŻeby sprawdzić kolejne liczby wpisz 1, żeby wyjść dowolną inną liczbę.\n--------------------------------------------------------------------------\n"))


    
input("--------koniec, naciśnij dowolny przycisk by kontynuować--------\n")
