class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barks")



class DogChild(Dog):
    def eats(self):
        print("Drinking Milk")

dog =Dog()            # this is the object
dog.bark()
dog.speak()
dogMdogo = DogChild()
dogMdogo.bark()
dogMdogo.speak()
dogMdogo.eats()