"""hm12_job1"""


class Bank:

    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name):
        self.clients[client_id] = {"name": name, "deposits": []}

    def open_deposit_account(self, client_id, start_balance, years, rate=0.1):
        if client_id in self.clients:
            deposit = {
                "start_balance": start_balance,
                "years": years,
                "rate": rate
            }

            self.clients[client_id]["deposits"].append(deposit)

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            return "invalid client_id"

        return round(sum(
            deposit["start_balance"] * (1 + deposit["rate"] / 12) ** (12 * deposit["years"])
            for deposit in self.clients[client_id]["deposits"]), 2)

    def close_deposit(self, client_id):
        if client_id in self.clients:
            self.clients[client_id]["deposits"] = []


client_id_01 = "0000001"  # pylint: disable=invalid-name

bank = Bank()
bank.register_client(client_id=client_id_01, name="Siarhei")
bank.open_deposit_account(client_id=client_id_01, start_balance=1000, years=1)
assert bank.calc_interest_rate(client_id=client_id_01) == 1104.71
bank.close_deposit(client_id=client_id_01)
