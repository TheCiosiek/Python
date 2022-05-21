import threading

# making class of threading.Thread
class myThread (threading.Thread):
  
   def __init__(self, thread_id, name, start_i, end_i):
       # Because the *args and **kwargs values passed to the Thread 
       # constructor are saved in private variables, they are not 
       # easily accessed from a subclass. To pass arguments to a custom 
       # thread type, we need to redefine the constructor to save the values 
       # in an instance attribute that can be seen in the subclass:
      threading.Thread.__init__(self)
      self.thread_id = thread_id
      self.name = name
      self.start_i = start_i
      self.end_i = end_i

   def run(self):
      print ("Starting " + self.name + self.thread_id)
      for i in range (self.start_i, self.end_i):
        lock.acquire()
        print ("nr: ", self.thread_id, "watek: ", self.name, "liczba:", i)
        lock.release()

lock = threading.Lock()

watek1 = myThread("1", "watek", 1, 5)
watek2 = myThread("2", "WATEK", 2, 8)

watek1.start()
watek2.start()

# watek1.join()
# watek2.join()

print ('Koniec programu')
