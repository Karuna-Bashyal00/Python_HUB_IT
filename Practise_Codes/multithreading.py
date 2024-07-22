
# note: Using Thread Module
# import threading
# import time

# def print_numbers():
#     for i in range(1,6):
#         time.sleep(1)
#         print(i)
        
# def print_letters():
#     for letter in 'abcde':
#         time.sleep(1.5)
#         print(letter)

# ?Creating Threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# ?Start Threads
# thread1.start()
# thread2.start()

# ?Wait for threads to complete
# thread1.join()
# thread2.join()

# note: Using Thread Subclass
import threading
import time

class NumberThread(threading.Thread):
    def run(self):
        for i in range(1,6):
            time.sleep(1)
            print(i)

class LetterThread(threading.Thread):
    def run(self):
        for letter in 'abcde':
            time.sleep(1.5)
            print(letter)

thread1 = NumberThread()
thread2 = LetterThread()

thread1.start()
thread2.start()


