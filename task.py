from banking import Bank, Client


def main():
    elliot = Client("Elliot", cash=1337)
    tyrell = Client("Tyrell", cash=64645435)
    allsafe = Client("Allsafe", cash=0)

    ebank = Bank(name="Evil Corp", clients=[tyrell], accounts={tyrell: 500})
    bbank = Bank(name="B2BB")

    ebank.register(elliot)
    bbank.register(allsafe)

    print(elliot)
    print(tyrell)
    print(allsafe)

    ebank.deposit(elliot, 1337)
    print("Elliot has ${} on his account (from deposit)".format(ebank.checkbalance(elliot)))
    print(elliot)

    ebank.deposit(tyrell, 500000)
    print("Tyrell has ${} on his account (from deposit and starting balance)".format(ebank.checkbalance(tyrell)))

    ebank.transfer(tyrell, bbank, allsafe, 500499)
    print("Allsafe's account balance: ${}".format(bbank.checkbalance(allsafe)))
    print("Tyrell after transfer: ${}".format(ebank.checkbalance(tyrell)))
    ebank.unregister(tyrell)
    print("Is Tyrell alive (as in a customer of the bank)? {}".format(ebank.is_client(tyrell)))

# Improvements:
# JSON to save to / read from file
# 3 Banks, 12 Customers, 16 Transactions
# credit (how much bank can give you)
