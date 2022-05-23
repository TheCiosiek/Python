#Adrian Szyłak, 20653
import socket
import time
import threading

# making class of threading.Thread
class makeThread (threading.Thread):
  
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        msg = self.conn.recv(2048)
        print("Start watku: %s Adres klienta: %s" % (self.name, self.addr))
        #Zobaczenie czy wątki działają równolegle
        if self.name == '0':
            time.sleep (10)
        comm = "Serwer-01 odpowiada: Otrzymalem komunikat od klienta = ".encode("utf-8")

        lock.acquire()
        print ("SERWER: Otrzymałem od klienta komunikat = ", msg)
        self.conn.send(comm + msg)
        lock.release()
        self.conn.close()

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
        

def init_server():
    start_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_serv.bind(("localhost", 2222))
    start_serv.listen(1)
    return start_serv


if __name__ == "__main__":
    lock = threading.Lock()
    print ("Start serwera port 2222\n")
    serv = init_server()
    while True:
        print ("Czekam na komunikat od klienta")
        new_conn, addr = serv.accept()
        threads_id = []
        #Sprawdzenie numerów wątków
        for thread in threading.enumerate():
            threads_id.append(thread.getName())
        #Znalezienie wolnego id nowego wątku
        for thread_id in range (len(threads_id)+1):
            if str(thread_id) not in threads_id:
                break
        new_thread = makeThread(new_conn, addr)
        new_thread.setName(thread_id)
        new_thread.start()
