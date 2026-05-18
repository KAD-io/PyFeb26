from logging import getLogger

LOGGER = getLogger(__name__)


class Bank:

    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name):
        self.clients[client_id] = {"name": name, "deposits": []}
        LOGGER.info('ID "%s" -> Name "%s"', client_id, name)

    def open_deposit_account(self, client_id, start_balance, years, rate=0.1):
        if client_id in self.clients:
            deposit = {
                "start_balance": start_balance,
                "years": years,
                "rate": rate
            }
            self.clients[client_id]["deposits"].append(deposit)
            LOGGER.info('for ID "%s" -> successfully', client_id)
            return True
        else:
            LOGGER.error('ID "%s" is not registered', client_id)
            return False

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            LOGGER.error('ID "%s" is not registered', client_id)
            return None

        result = round(sum(
            deposit["start_balance"] * (1 + deposit["rate"] / 12) ** (12 * deposit["years"])
            for deposit in self.clients[client_id]["deposits"]), 2)
        LOGGER.info('for ID "%s" -> %s', client_id, result)
        return result

    def close_deposit(self, client_id):
        if client_id in self.clients:
            self.clients[client_id]["deposits"] = []
            LOGGER.info('for ID "%s"  -> successfully', client_id)
            return True

        LOGGER.error('ID "%s" is not registered', client_id)
        return False
