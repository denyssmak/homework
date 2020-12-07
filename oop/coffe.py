class CoffeMachine:
    water = 50
    grains = 50
    _curent_trash = 0  
    __max_trash = 40

    
    def espresso(self): 
        if self._isfull(10):
            self.clear()
            print("Кофеварка заполнeна мусором")
        elif self.water < 10 and self.grains < 5:
            self.clear()
            print("закончились зерна или вода") 
        else:
            self.water -= 10
            self.grains -= 5
            self._curent_trash += 10
            print("espresso готов")

    def americano(self):
        if self._isfull(10):
            self.clear()
            print("Кофеварка заполнeна мусором")
        elif self.water < 10 and self.grains < 10:
            self.clear()
            print("закончились зерна или вода")
        else:
            self.grains -= 10
            self.water -= 10
            self._curent_trash += 10
            print("americano готов") 
        
    def clear(self): 
        if self.water <= 10:
            self.water = 25 
        if self.grains <= 10:
            self.grains = 25 
        else:
            self._curent_trash = 0
        
    def _isfull(self,trash):
        return self._curent_trash + trash > self.__max_trash

class Coffe_and_Milk(CoffeMachine):
    milk = 50

    def add_milk(self): 
        if self.milk <= 0:
            self.updateMilk()
            print("закончилось молоко")
        else:
            self.milk -= 10
        print("молоко добавленно") 


    def updateMilk(self):
        self.milk = 50  

class Liquor(Coffe_and_Milk):
    liquor = 25
    
    def add_liquor(self): 
        if self.liquor < 5:
            self.updateLiquor()
            print("ликера нету!!!")
        else:
            self.liquor -= 5
        print("liquor")


    def updateLiquor(self):
        self.liquor = 25


    def late(self):
        if self._isfull(10):
            self.clear()
            print("Кофеварка заполнeна мусором")
        elif self.water < 10 and self.grains < 5:
            self.clear()
            print("закончились зерна или вода") 
        else:
            self.water -= 10
            self.grains -= 5
            self._curent_trash += 10
            print("late готов")

    def cappuccino(self):
        if self._isfull(10):
            self.clear()
            print("Кофеварка заполнeна мусором")
        elif self.water < 5 and self.grains < 10:
            self.clear()
            print("закончились зерна или вода") 
        else:
            self.water -= 5
            self.grains -= 10
            self._curent_trash += 25
            print("cappuccino готов")

    
coffe = Coffe_and_Milk()
a = Liquor()
[a.cappuccino() for i in range(20)]
