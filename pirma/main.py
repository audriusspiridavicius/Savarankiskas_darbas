from BankAccount import BankAccount

account = BankAccount("123456789")
print(account)

account.deposit(100)
print(account)

amount = account.withdraw(200)
print(f"amount = {amount}")
print(account)

#should still add 500 to account
account.deposit(-500)
print(account)

#balance of the account shouldn't change
account.withdraw("156g")
print(account)