from abc import ABC, abstractmethod

class Computer(ABC):
    #Abscract class
    @abstractmethod
    def Turn_on(self):
        pass

    @abstractmethod
    def Turn_off(self):
        pass


class Computer_w_rgb(Computer):

    
    def Turn_on(self):
        self.is_turned_on = True
        return "Computer was turned on!"
    
    def Turn_off(self):
        self.is_turned_on = False
        return "Computer was turned off!"
    
    def Enable_rgb(self):
        self.is_rgb_enabled = True
        return "Rgb was enabled"



if __name__ == "__main__":
    
    gaming_computer = Computer_w_rgb()#creating computer object

    gaming_computer.Turn_on()

    gaming_computer.Turn_off()

    gaming_computer.Enable_rgb()
    

    
        
