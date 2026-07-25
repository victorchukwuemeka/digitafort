import time 

# a car 
class Car :
    #our contruct with all the default data 
    def __init__(self, make , model):
        self.make = make 
        self.model = model 
        self._is_it_running = False 
        self._speed = 0
        self._fuel_l = 100.0


    # hidden  functions 
    def _check_fuel(self):
        if self._fuel_l > 0:
            return True 
        else :
            return False 

    def _ignite_spark_plug():
        time.sleep(0.5)

    def _used_fuel(self):
        self._fuel_l -= 2.5
        time.sleep(0.5)

     
    