from banking import banking
bobj = banking()
bobj.account_create()
account1=bobj.account_create()
account2 = bobj.account_create()

bobj.deposit(account1, 20)
bobj.deposit(account2, 40)
bobj.deposit(account1, 50)
bobj.transfer(account1,account2,10)

statements = bobj.account_statement(account1)
print(statements)