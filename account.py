class Account:
    bank = "money"
    def __init__(self,accountName,accountNumber,password,bank):
        self.accontName = accountName
        self.accountNmber = accountNumber
        self.password = password
        self.bank = bank

    def widthraw(self):
        return f"I have less {self.bank} thus i cant widthraw"
    def balance(self):
        return f"I have less {self.bank} in my account"
    def deposit(self):
        return f"I have deposit some amont in my {self.accountNmber}"

                 