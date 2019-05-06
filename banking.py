class Client():

    def __init__(self, name="Anonymous", cash=0):
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

    def addcash(self, amt):
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
