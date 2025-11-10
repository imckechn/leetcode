from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = {}

        for i in range(len(balance)):
            self.accounts[i+1] = balance[i]

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if  (
            account1 in self.accounts.keys() and 
            account2 in self.accounts.keys() and 
            self.accounts[account1] >= money
            ):
            self.accounts[account1] -= money
            self.accounts[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.accounts.keys():
            self.accounts[account] += money
            return True
        return False
        
    def withdraw(self, account: int, money: int) -> bool:
        if account in self.accounts.keys() and self.accounts[account] >= money:
            self.accounts[account] -= money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
obj = Bank([10,100,20,50,30])

ans = obj.withdraw(3,10)
if ans != True:
    print("A Failed")

ans = obj.transfer(5,1,20)
if ans != True:
    print("B Failed")

ans = obj.deposit(5,20)
if ans != True:
    print("C Failed")

ans = obj.transfer(3,4,15)
if ans != False:
    print("D Failed")
    
ans = obj.withdraw(10,50)
if ans != False:
    print("E Failed")

# ["Bank",              "withdraw",  "transfer",  "deposit",  "transfer",   "withdraw"]
# [[[10,100,20,50,30]], [3,10],      [5,1,20],     [5,20],     [3,4,15],    [10,50]]