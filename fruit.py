class Fruit:
    fruit_count=0

    def __init__(self,color,taste,shape,preference):
        self.color=color
        self.taste=taste
        self.shape=shape
        self.preference=preference
        

        Fruit.fruit_count += 1
        self.fruit_number+Fruit.fruit_count

    def get_shape(self):
        return self.shape
    
    def set_shape(self,new_shape):
        self.shape=new_shape

    def increase_preference(self):
        self.preference = self.preference+1
    
    def showFruit(self):
        print("This is Fruit {self.fruit_number}")
        print("color: {},shape: {},Taste: {},Preference: {}".format(self.color,self.shape,self.taste,self.preference))


        print("----------------------------")
    
apple=Fruit("red","sweet","round",1)
apple.showFruit()
apple.increase_preference()

print("Shape of fruit",apple.fruit_number,":",apple.get_shape)
apple.set_shape("sphere")
apple.showFruit()

banana=Fruit("Yellow","sweet","Cylinder",2)
banana.showFruit()
banana.increase_preference()
banana.showFruit()