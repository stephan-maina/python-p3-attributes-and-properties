APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Mastiff"):
        self.name = name
        self.breed = breed
        self.tricks = []

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (isinstance(name, str)) and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in the list of approved breeds.")

    breed = property(get_breed, set_breed)

    def bark(self):
        return f"{self.name} says Woof!"

    def learn_trick(self, trick):
        self.tricks.append(trick)
        return f"{self.name} learned {trick}!"

    def do_tricks(self):
        if self.tricks:
            return f"{self.name} can do tricks: {', '.join(self.tricks)}"
        else:
            return f"{self.name} hasn't learned any tricks yet."

    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nTricks: {', '.join(self.tricks)}"

if __name__ == "__main__":
    dog1 = Dog("Chess", "Golden Retriever")
    dog2 = Dog("Max")

    print(dog1.bark())
    print(dog2.bark())

    print(dog1.learn_trick("Sit"))
    print(dog1.learn_trick("Roll Over"))

    print(dog1.do_tricks())
    print(dog2.do_tricks())

    print("Dog 1 Info:")
    print(dog1)

    print("Dog 2 Info:")
    print(dog2)
