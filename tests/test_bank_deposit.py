import unittest

from source.bank_deposit import Bank


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.client_id = "0000001"
        self.client_name = "John Smith"

    def test_register_client_success(self):
        """Positive test: client registration"""
        self.bank.register_client(self.client_id, self.client_name)
        self.assertIn(self.client_id, self.bank.clients)
        self.assertEqual(self.bank.clients[self.client_id]["name"], self.client_name)

    def test_open_deposit_success(self):
        """Positive test: opening a deposit"""
        self.bank.register_client(self.client_id, self.client_name)
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        self.assertEqual(len(self.bank.clients[self.client_id]["deposits"]), 1)
        self.assertEqual(self.bank.clients[self.client_id]["deposits"][0]["start_balance"], 1000)

    def test_calc_interest_rate_correctness(self):
        """Positive test: rate calculation"""
        self.bank.register_client(self.client_id, self.client_name)
        self.bank.open_deposit_account(self.client_id, 1000, 1, rate=0.1)
        expected_result = 1104.71
        result = self.bank.calc_interest_rate(self.client_id)
        self.assertEqual(result, expected_result)

    def test_close_deposit_success(self):
        """Positive test: closing deposits"""
        self.bank.register_client(self.client_id, self.client_name)
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        expected_result = True
        result = self.bank.close_deposit(self.client_id)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(self.bank.clients[self.client_id]["deposits"]), 0)

    def test_open_deposit_unregistered_client(self):
        """Negative tests: open deposit for non-existent ID should return False"""
        expected_result = False
        result = self.bank.open_deposit_account("non_existent_id", 1000, 1)
        self.assertEqual(result, expected_result)

    def test_calc_interest_unregistered_client(self):
        """Negative tests: Interest calculation for non-existent customer should return None"""
        result = self.bank.calc_interest_rate("non_existent_id")
        self.assertIsNone(result)

    def test_close_deposit_unregistered_client(self):
        """Negative tests: Closing the deposit of non-existent client should return False"""
        expected_result = False
        result = self.bank.close_deposit("non_existent_id")
        self.assertEqual(result, expected_result)
