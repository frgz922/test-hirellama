from helpers import Timer
import time
import random

def get_random_number():
    number = random.randint(0,22) 
    print(number)
    
    
def print_msg(msg):
    print(msg)
    

def main(fun):
    t = Timer()
    t.start()
    fun
    time.sleep(random.randint(1,30))
    t.stop()


if __name__ == "__main__":
    main(get_random_number())
    main(print_msg('Hi! I am a message!')) 
    