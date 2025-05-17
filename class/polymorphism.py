class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):  # Overrides parent method
        print("Penguins cannot fly")

bird = Bird()
penguin = Penguin()
bird.fly()      # Output: Birds can fly
penguin.fly()   # Output: Penguins cannot fly
Bird().fly()