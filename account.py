class Account():

    def __init__(self,name,accnum,pword):

        self.hasaccount=True

        self.name=name

        self.accnum=accnum

        self.pword=pword

        self.balance=0



    def closeaccount(self,name,accnum,pword):

        if self.name==name and self.accnum==accnum and self.pword==pword:

            self.hasaccount=False

        else:

            print("\n invalid credential, unable to close account")



    def  checkbalance(self,accnum,pword):

        if self.accnum==accnum and self.pword==pword:

            print("\n your balance is ",self.balance)

        else:

            print("\n invalid credential, cannot show balance")

    def deposite(self,accnum,balance):

        if self.accnum==accnum:

            if balance>0:

                self.balance=self.balance+balance

                print("\n ammount deposited")

            else:

                print("\n can not deposite this amount")

        else:

            print("\n invalid credential ")



    def withdraw(self,accnum,balance,pword):

        if self.accnum==accnum and self.pword==pword:

            if balance>0 and self.balance>=balance:

                self.balance=self.balance-balance

                print("\n amount withdrawn")

                print('\n remaining balance: ',self.balance)

            else:

                print("\n can not withdrwa this amount")

        else:

            print("\n invalid credential ")



    def display_info(self,accnum,pword):



        if self.accnum == accnum and self.pword == pword:

            print("\n name: ",self.name)

            print("\n account no: ",self.accnum)

            print("\n available balance: ",self.balance)

        else:

            print("\n enter correct details to see information")


