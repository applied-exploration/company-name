import random
import time

def random_sleep(min:int=0.1, max:int=3.5)->None:
    time.sleep(random.uniform(min, max))