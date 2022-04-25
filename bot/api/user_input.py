class UserInput:
    name = ''
    amount = 0

    def __init__(self, name, x):
        self.amount = x
        self.name = name

    def print_data(self):
        print(self.name, self.amount)
