# changes made in an instance object affect only that instance

class PaySlips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name 
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = 'yes'

    def status(self):
        if self.payment == 'yes':
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan = PaySlips("Nathan", "no", 1000)
roger = PaySlips("Roger", "no", 3000)

print(nathan.status(), "\n" , roger.status())

nathan.pay()
print("After payment")
print(nathan.status(), "\n" , roger.status())
