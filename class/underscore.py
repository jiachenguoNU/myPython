class UnderScore:
    def __init__(self, name, hometown):
        self.name = name
        self.__hometown = hometown

    def card(self):
        return print(f"name: {self.name}, hometown: {self.__hometown}")
    
    def set_att(self, home_town):
        self.__hometown = home_town



card0 = UnderScore("John", "New York")
card0.card()
card0.set_att('Chicago')
card0.card()

print(card0.__hometown)  # Output: AttributeError: 'UnderScore' object has no attribute '__hometown'