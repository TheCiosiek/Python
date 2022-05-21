#Program klient dla programowania socket
#KLIENT
#
#Dałączenie biblioteki
import socket

#Program Klient:
#- wczytuje komunikat z klawiatury,
#- zestawia połączenie z serwerem
#- nadaje wczytany komunikat do serwera
#- odbiera komunikatu odpowiedzi z serwera
#- listuje odebrany komunikat na ekranie
#- rozłaczenie połaczenia z serwerem
#

#Program główny pętla nieskończona
while 1:
    #Tworzenie gniazdka (socket), AF_INET - adresacja IPv4,
    #SOCK_STREAM - gniazdko dla przesyłania strumieniowego,
    #domyślnie wybrany protokół TCP
    gniazdko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Obsługa wyjatku dla utworzenia socket
    try:
        #socket - gniazdko utworzone
        #Nawiązanie połączenia z serwerem pod adresem 127.0.0.1 nr. port serwera = 2222
        #W instrukcji poniżej muszą być podwójne nawiasy
        gniazdko.connect(("127.0.0.1", 2222))
        #wczytanie z klawiatury wysyłanego komunikatu
        kom_str = input ("Klient_1 Podaj komunikat = ")
        #Wysyłany komunikat musi być zakończony dwa razy powrót karetki, nowa linia
        kom_str = kom_str + "\r\n\r\n"
        #Zamiana wczytanego łańcucha znaków (string) na ciąg bytes
        kom_bytes  = kom_str.encode("utf-8")
        #Nadawanie komunikatu do serwera
        gniazdko.send(kom_bytes)                                      
        #Odbiór komunikatu z serwera (długość komunikatu max 2048 bajtów 
        komunikat_serwer = gniazdko.recv(2048)
        #Wydruk odebranego komunikatu z serwera
        print (komunikat_serwer)
    #Początek procedury obsługi błędu w operacjach na socket
    except socket.error:
        pass
    #Zawsze wykonywane niezależnie od błędu
    finally:
        #Koniec pętli, zamkniecie socket
        gniazdko.close()

#Koniec programu


