import unittest
from banking import Bank, Client


class BankingTests(unittest.TestCase):

    def test_init_client(self):
        c = Client()
        self.assertEqual(c.name, 'Anonymous')
        self.assertEqual(c.cash, 0)

    def test_named_client(self):
        c = Client(name="Test", cash=100)
        self.assertEqual(c.name, 'Test')
        self.assertEqual(c.cash, 100)

    def test_pay(self):
        c2 = Client(cash=100)
        self.assertFalse(c2.pay(101))

    def test_pay2(self):
        c1 = Client(cash=500)
        self.assertTrue(c1.pay(101))
        self.assertEqual(c1.cash, 500-101)

    def test_pay_neg(self):
        c1 = Client(cash=400)
        c1.pay(-1)
        self.assertEqual(c1.cash, 401)

    def test_addcash(self):
        c1 = Client(cash=500)
        c1.addcash(1)
        self.assertEqual(c1.cash, 501)

    def test_addcash_neg(self):
        c1 = Client(cash=500)
        c1.addcash(-1)
        self.assertEqual(c1.cash, 499)

    def test_init_bank(self):
        g = Client()
        b = Bank(name="Bank", clients=[g], accounts={g:1})
        self.assertTrue(g in b.clients)

    def test_is_client(self):
        g = Client()
        b = Bank(name="Bank", clients=[g], accounts={g:1})
        self.assertTrue(b.is_client(g))

    def test_is_not_client(self):
        b = Bank()
        self.assertFalse(b.is_client("Goethe"))

    def test_registered(self):
        g = Client(name="Goethe")
        b = Bank(name="Bank", clients=[g], accounts={g:1})
        self.assertFalse(b.register(g))

    def test_register(self):
        g = Client()
        b = Bank()
        self.assertTrue(b.register(g))
        self.assertTrue(b.is_client(g))

    def test_unregister(self):
        g = Client(cash=100)
        b = Bank(clients=[g], accounts={g: 200})
        self.assertEqual(b.unregister(g), 200)

    def test_unregistered(self):
        g = Client()
        b = Bank()
        self.assertFalse(b.unregister(g))

    def test_checkbalance(self):
        g = Client()
        b = Bank(clients=[g], accounts={g: 100})
        self.assertEqual(b.checkbalance(g), 100)

    def test_deposit(self):
        g = Client(cash=500)
        b = Bank()
        self.assertFalse(b.deposit(g, 100))

    def test_deposit2(self):
        g = Client(cash=100)
        b = Bank()
        b.register(g)
        self.assertTrue(b.deposit(g, 100))

    def test_deposit3(self):
        g = Client(cash=100)
        b = Bank()
        b.register(g)
        self.assertFalse(b.deposit(g, 101))

    def test_transfer(self):
        g = Client(cash=100)
        c = Client(cash=200)
        b = Bank()
        b.register(g)
        b.register(c)
        b.deposit(g, 100)
        b.deposit(c, 200)
        b.transfer(g, b, c, 100)
        self.assertEqual(b.checkbalance(c), 300)

    def test_crossbanktransfer(self):
        g = Client(cash=400)
        c = Client()
        b = Bank()
        b2 = Bank()
        b.register(g)
        b2.register(c)
        b.deposit(g, 400)
        b.transfer(g, b2, c, 400)
        self.assertEqual(b2.checkbalance(c), 400)


if __name__ == '__main__':
    unittest.main()
