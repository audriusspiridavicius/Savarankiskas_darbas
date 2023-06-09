class BankAccount:
    def __init__(self, account, balance=0):
        self.account = account
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = self.__format_number(value)

    def deposit(self, number):
        """

        :param number: number you want to add to your account
        :return: return amount you successfully added
        """
        self.balance += number
        return number

    def withdraw(self, number):
        """
        :param number:amount that will withdraw from the account
        :return:returns what amount was withdrawn
        """
        number = self.__format_number(number)
        if number > self.balance:
            number = self.balance
        self.balance -= number
        return number

    def __format_number(self, number):
        try:
            number = abs(float(number))
        except ValueError:
            print(f"You have entered invalid number. Entered value : {number}")
            return 0
        else:
            return number

    def __str__(self):
        return f"Your bank account number: {self.account}\nYour current balance: {self.balance}\n"
