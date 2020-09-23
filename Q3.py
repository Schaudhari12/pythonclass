class Car:
  def __init__(self, model, make, electric):
    self.model = model
    self.make = make
    self.electric = electric

  def display(self):
    print("model " + self.model + ", make " + self.make + ", electric " + str(self.electric))
  def start(self):
    print("You are in start")

c1 = Car("S3", "Tesla", 1)



c2 = Car("Sienna", "Toyota", 1)


c3 = Car("C240", "Mercedes", 1)


carlist = [c1, c2, c3]
for car in carlist:
	car.display()