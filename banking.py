import pandas as pd
from collections import defaultdict
from datetime import datetime

## {'acount': [{'type': deposit,'amount':20, 'timestamp':datetime}]}

class banking:

    def __init__(self):
        self.tracker = {}
        self.mybank = pd.DataFrame(columns=['account','total','transactions'])
        self.start = 1

    
    def _transactions(self,account:int,type:str,amount:int)->None:
        self.tracker[account]['transactions'].append({'type':type, 'amount':amount, 'timestamp':datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    

    def account_create(self) ->int:
        self.tracker[self.start] = {'total':0,
                                    'total_transactions':0,
                                    'transactions':[]}

        self.mybank.loc[len(self.mybank)]= [self.start, 0, 0]

        self.start+=1
        print(f"Account created. Account no - {self.start-1}")
        return self.start-1
    

    def deposit(self,account:int,amount:float)->bool:
        if account not in self.tracker:
            print(f"Account no {account} not found!")
            return False
        
        self.tracker[account]['total']+=amount
        self.tracker[account]['total_transactions']+=1
        self._transactions(account,type='deposit',amount=amount)

        return True
    

    def withdraw(self, account:int, amount:float)->bool:
        if account not in self.tracker or self.tracker[account]['total']<amount:
            return False
        
        self.tracker[account]['total']-=amount
        self.tracker[account]['total_transactions']+=1
        self._transactions(account,type='withdraw',amount=amount)

        return True
    

    def transfer (self, depositor:int, recipient:int, amount:float)->bool:
        if recipient not in self.tracker or depositor not in self.tracker or self.tracker[depositor]['total']<amount:
            return False
        
        self.tracker[depositor]['total']-=amount
        self.tracker[recipient]['total']+=amount
        self.tracker[depositor]['total_transactions']+=1
        self.tracker[recipient]['total_transactions']+=1

        self._transactions(depositor,type='transfer out',amount=amount)
        self._transactions(recipient,type='transfer in',amount=amount)

        return True
    

    def account_statement(self, account:int)->list:
        return self.tracker[account]['transactions']



    
