class BankCard():
    def __init__(self, owner, number, provider):
        self.owner=owner
        self.number=number
        self.provider=provider
    def get_numer():
        pass
    def get_owner():
        pass
    def get_provider():
        pass
class BankAccount:
    def __init__(self, owner, balance, bank):
        self.own=own
        self.bal=bal
        self.babk=bank
    def get_owner(self):
        pass
    def get_balance(self):
        pass
    def get_bank():
        pass
    def set_balance(self):
        pass
class Bank:
    def __init__(self, name, bank_accounts, bank_cards):
        self.name=name
        self.bank_accounts=bank_accounts
        self.bank_cards=bank_cards
    def get_bank_accounts(self):
        pass
    def get_bank_cards(self):
        pass
class CreditCard(BankCard):
    def __init__(self, owner, number, provider, balance, payment_history):
        super().__init__(owner, number, provider)
        self.balance=balance
        self.payment_history=payment_history
    def get_balance():
        pass
    def set_balance():
        pass
    def get_payment_history():
        pass
class GoldenCreditCard(CreditCard):
    def __init__(self, owner, number, provider, balance, payment_history,reward_points):
        super().__init__(owner, number, provider, balance, payment_history)
        self.reward_points=reward_points
class PremiumBankAccount(BankAccount):
    def __init__(self, name, bank_accounts, bank_cards,financial_manager):   
        super().__init__(self, name, bank_accounts, bank_cards)
        self.financial_manager=financial_manager
    def get_financial_manager():
        pass
    def set_financial_manager():
        pass
class StudentBankAccount(BankAccount):
    def __init__(self, name, bank_accounts, bank_cards, overdraft_balance, overdraft_limit):   
        super().__init__(self, name, bank_accounts, bank_cards)
        self.overdraft_balance=overdraft_balance
        self.overdraft_limit=overdraft_limit
    def get_over_draft_balance():
        pass
    def set_overdraft_balance():
        pass
    def get_overdraft_limit():
        pass
    def set_overdraft_limit():
        pass