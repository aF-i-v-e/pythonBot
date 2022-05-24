class UserInput:
    name = ''
    amount = 0
    month_count = 0

    def __init__(self, name, amount, month_count):
        self.name = name
        self.amount = amount
        self.month_count = month_count

    def print_data(self):
        print('Имя: ' + str(self.name) + '   Сумма: ' + str(self.amount) + '   Срок: ' + str(self.month_count))

    def get_amount(self):
        return self.amount

    def get_month_count(self):
        return self.month_count

    def get_string_representation(self):
        s1 = f"Уважаемый пользователь {self.name}!\n" \
             f"Ваша начальная сумма вклада составляет {str(self.amount)} рублей.\n"
        if self.month_count == 0:
            return s1 + "Срок вклада: произвольный.\n"
        return s1 + f"Срок вклада: {self.month_count}.\n"

    def set_name(self, new_name):
        self.name = new_name

    def set_amount(self, new_amount):
        self.amount = new_amount

    def set_month_count(self, new_term):
        self.month_count = new_term
