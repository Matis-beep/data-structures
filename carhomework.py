class Car:
    def __init__(self, colour, brand, model):
        self._colour = colour
        self._brand = brand
        self._model = model

    
    def get_colour(self):
        return self._colour

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

   
    def set_colour(self, new_colour):
        self._colour = new_colour

brand = input("Enter car brand: ")
model = input("Enter car model: ")
colour = input("Enter car colour: ")


car = Car(colour, brand, model)


print("\nCar Details:")
print("Brand:", car.get_brand())
print("Model:", car.get_model())
print("Colour:", car.get_colour())


new_colour = input("Enter new colour to update: ")
car.set_colour(new_colour)


print("Updated Car Details:")
print("Brand:", car.get_brand())
print("Model:", car.get_model())
print("Color:", car.get_colour())