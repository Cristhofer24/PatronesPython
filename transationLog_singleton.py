import copy

class TransactionLogger:
    _instance=None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TransactionLogger, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.log_file = "transaction_log.csv"
            
    def log(self,message):
        with open(self.log_file,"a") as f:
            f.write(message+"\n")
        print(f"Log Registrado:{message}")
        
#Verificacion 
logger1 = TransactionLogger()
logger2 = TransactionLogger()

print(logger1 is logger2)

class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposito(self,amount):
        self.balance += amount
        message = f"{self.account_holder} depositó ${amount}. Nuevo saldo: ${self.balance}"
        TransactionLogger().log(message)
        
    def retiro(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            message = f"{self.account_holder} retiro ${amount}. Nuevo saldo: ${self.balance}"
        else:
            message = f"{self.account_holder} no puede retirar ${amount}. Saldo insuficiente."
           
        TransactionLogger().log(message)
         
#Pruebas 
user1 = BankAccount("John Doe",1000)
user2 = BankAccount("Jane Doe",2000)

#Trasacciones
user1.deposito(500)
user1.retiro(200)
user1.retiro(5000)

user2.deposito(1000)
user2.retiro(3000)

