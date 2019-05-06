class Client():

    def __init__(self, name = "Anonymous", cash = 0):
        self.name = name
        self.cash = cash

    def __repr__(self):
        return "<Client {} with ${} in cash>".format(self.name, self.cash)

    def pay(self, amt):
        if (self.cash-amt) >= 0:
            self.cash -= amt
            return True
        else:
            return False

    def addcash(self,amt):
        self.cash += amt
        return self.cash

class Bank():

    def __init__(self, name="", clients=[], accounts={}):
        self.name = name
        self.clients = clients
        self.accounts = accounts

    def is_client(self, client):
        return client in self.clients

    def withdraw(self, client, amt):
        if self.is_client(client):
            self.accounts[client] -= amt
            return amt
        else:
            return False

    def deposit(self, client, amt):
        if self.is_client(client) and client.pay(amt):
            self.accounts[client] += amt
            return True
        else:
            return False

    def transfer(self, client, targetbank, target, amt):
        if self.is_client(client):
            if targetbank == self and self.is_client(target):
                self.accounts[client] -= amt
                self.accounts[target] += amt
                return True
            elif targetbank.is_client(target):
                self.accounts[client] -= amt
                targetbank.accounts[target] += amt
                return True
            else:
                return False
        else:
            return False

    def checkbalance(self, client):
        if self.is_client(client):
            return self.accounts[client]

    def register(self, client):
        if self.is_client(client):
            return False
        else:
            self.clients.append(client)
            self.accounts[client] = 0
            return True

    def unregister(self, client):
        if self.is_client(client):
            amt = self.withdraw(client, self.accounts[client])
            self.accounts[client] = None
            self.clients.remove(client)
            return amt
        else:
            return False

def main():
    elliot = Client("Elliot", cash = 1337)
    tyrell = Client("Tyrell", cash = 64645435)
    allsafe = Client("Allsafe", cash = 0)

    ebank = Bank(name="Evil Corp",clients=[tyrell],accounts={tyrell: 500})
    bbank = Bank(name="B2BB")

    ebank.register(elliot)
    bbank.register(allsafe)

    print(elliot)
    print(tyrell)
    print(allsafe)

    ebank.deposit(elliot, 1337)
    print("Elliot has ${} on his account (from deposit)".format(ebank.checkbalance(elliot)))
    print(elliot)

    ebank.deposit(tyrell,500000)
    print("Tyrell has ${} on his account (from deposit and starting balance)".format(ebank.checkbalance(tyrell)))

    ebank.transfer(tyrell, bbank, allsafe, 500499)
    print("Allsafe's account balance: ${}".format(bbank.checkbalance(allsafe)))
    print("Tyrell after transfer: ${}".format(ebank.checkbalance(tyrell)))
    ebank.unregister(tyrell)
    print("Is Tyrell alive (as in a customer of the bank)? {}".format(ebank.is_client(tyrell)))


if __name__ == '__main__':
    main()

# Improvements:
# JSON to save to / read from file
# 3 Banks, 12 Customers, 16 Transactions
# credit (how much bank can give you)
