class bank:
    def __init__(self,acc_no,balance=0):
        self.acc_no=acc_no
        self.balance=balance
    def deposit_amount(self,amount):
        if amount>0:
            self.balance+=amount
            print("₹",amount,"successfully deposited to your bank account!!")
            print("total balance:","₹",self.balance)
        else:
            print("invalid amount")
    def withdraw_amount(self,amount):
        if amount<=self.balance and amount>0:
            self.balance-=amount
            print("₹",amount,"has been successfully withdrawn from your bank account!!")
            print("total balance:","₹",self.balance)
        else:
            print("insufficient balance!!")
    def check_balance(self):
        print("*"*100)
        print("ATM name: State Bank Of India!")
        print("account number:",self.acc_no)
        print("name of the account holder:",name)
        print("balance:","₹",self.balance)
        print("*"*100)
name=input("enter account holder's name:")
ac=int(input("enter acc no:"))
bal=float(input("enter balance:"))
your_account=bank(ac,bal)
while True:
    print("what you want to do?: \n1. deposit some amount. \n2. withdraw some amount. \n3. check balance. \n4. exit.")
    ch=int(input("enter choice:"))
    if ch==1:
        your_deposit=float(input("enter amount you want to deposit:"))
        your_account.deposit_amount(your_deposit)
    elif ch==2:
        your_withdraw=float(input("enter amount you want to withdraw:"))
        your_account.withdraw_amount(your_withdraw)
    elif ch==3:
        your_account.check_balance()
    elif ch==4:
        print("thanks for visiting!!")
        break
    else:
        print("invalid choice!")
        break