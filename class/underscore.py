class UnderScore:
    def __init__(self, name, hometown):
        self.name = name
        self.__hometown = hometown

    def card(self):
        return print(f"name: {self.name}, hometown: {self.__hometown}")



card0 = UnderScore("John", "New York")
print(card0.name)  # Output: John
print(card0.__hometown)  # Output: AttributeError: 'UnderScore' object has no attribute '__hometown'