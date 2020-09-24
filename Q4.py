class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getPermit(self):
  	if self.age < 13:
          raise ValueError("Error, because you are less than 13 years old")
	 
s1 = Student("Sanika", 12)
try:
	# method which can raise exception
     s1.getPermit()
except ValueError as e:
	print(f"    Error:{e}")
