# -*- coding: cp936 -*-
class BankAccount:
    
    def __init__(self,acct_number,acct_name):
        self.acct_number = acct_number
        self.acct_name = acct_name
        self.balance = 0.0
        
    def displayBalance(self):
        print "The account balance is:",self.balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print "You deposited",amount
        print "The new balance is:",self.balance

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print "You withdrew",amount
            print"The new balance is:",self.balance
        else:
            print "You tried to withdraw",amount
            print "The account balance is:",self.balance
            print "WithDrawal denied. Not enough funds."

class InterestAccount(BankAccount):
    def __init__(self,acct_number,acct_name,rate):
        BankAccount.__init__(self,acct_number,acct_name)
        self.rate = rate
    def addInterest (self):
        interest = self.balance * self.rate
        print "adding interest to the account,",self.rate*100,"percent"
        self.deposit(interest)

myAccount = InterestAccount(234567,"Warren Sande",0.11)
print "Account Name:",myAccount.acct_name
print "Account Number:",myAccount.acct_number
myAccount.displayBalance()
myAccount.deposit(34.52)
myAccount.addInterest()
