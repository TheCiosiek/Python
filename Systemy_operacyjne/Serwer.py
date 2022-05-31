#Program Serwer dla programowania socket
# SERWER
#
#Dałączenie biblioteki
import socket
import time
from _thread import *

def multi_threaded_client(connection):
    # connection.send(str.encode('Server is working:'))
    data = connection.recv(2048)
    response = 'Server message: '.encode("utf-8") + data
    print(response)
    connection.send(response)
    connection.close()

ThreadCount = 0

#Funkcja inicjowania serwera
def init_server():
    # Tworzenie gniazdka (socket), AF_INET - adresacja IPv4,
    # SOCK_STREAM - gniazdko dla przesyłania strumieniowego,
    # Domyslnie wybrany protokół TCP
    gniazdo_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
    #Do gniazdka (socket) przyłączony jest port i adres IP
    #W instrukcji poniżej muszą być podwójne nawiasy
    gniazdo_serv.bind(("localhost", 2222))
    #Rozpocznij nasłuchiwanie
    gniazdo_serv.listen(1)
    #Funkcja init_server zwraca zainicjowany socket (gniazdko)
    return gniazdo_serv
#Koniec funkcji

#Komunikat wysyłany do klienta
#kom_str = "Serwer-01 odpowiada: Otrzymalem komunikat od klienta = "

#Program glowny
print ("\n\nStart Serwera Port 2222\n")
#Wywołanie funkcji init_server - inicjowania serwera
#gniazdko_serwera = init_server()
serv = init_server()
#Pętla nieskończona (1)
while True:
    #Oczekiwanie na zgłoszenie od klienta lub pobranie z kolejki
    #Funkcja accept zwraca nowe gniazdko dla obsługi zgłoszenia od klienta
    #jeżeli błąd to zwrot -1
    print ("\nCzekam na komunikat od klienta")
    nowe_gniazdko, addr = serv.accept()

    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    
    start_new_thread(multi_threaded_client, (nowe_gniazdko,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

gniazdo_serv.close()
