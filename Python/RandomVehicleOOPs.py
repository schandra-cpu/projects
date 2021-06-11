class Vehicle(object):
  def __init__(self, name, model, num_wheels):
    self._name = name
    self._model =  model
    self._number_of_wheels = num_wheels

  def __str__(self):
    return "Name: {0}, Model: {1}, Number of Wheels: {2}".format(self._name, self._model, self._number_of_wheels)
	
class Car(Vehicle):
  def __init__(self, model):
    super(Car, self).__init__("Car", model, 4)
	
class Bicycle(Vehicle):
  def __init__(self, model):
    super(Bicycle, self).__init__("Bicycle", model, 2)
	
if __name__ == "__main__":
  bike_1 = Bicycle("Hercules")
  car_1 = Car("Swift")

  print("Car 1:", car_1)
  print("Bike 1:", bike_1)