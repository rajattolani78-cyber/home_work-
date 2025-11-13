balance = 0.0
kyc_doc = {}
def check_balance():
    print(f"your current balance is {balance}")
def deposit(amount):
    global balance
    if amount > 0 :
       balance += amount
    else :
        print("can not deposit negatiove amount or zero amount")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("cannot withdraw negative or zero amount")
    elif amount > balance:
        print("can not withdraw. insufficent balance ")
    else:
        balance -= amount
def update_kyc(doc):
    global kyc_doc
    kyc_doc.update(doc)
def check_kyc():
        if len(kyc_doc)==0:
            print("kyc not done")
        else:
           for doc in kyc_doc:
            print(f"{doc}: {kyc_doc[doc]}")
print ("welcome to acb bank ATM system:")
while True :
    print("============================")
    print("1. check balance")
    print("2. deposit an amount")
    print("3. withdraw an amount")
    print("4. check kyc")
    print("5. update kyc")
    print("6. Quit")
    print("============================")
    choice = input ("Enter your choice (1-4): ")
    if choice == "1":
       check_balance()
    elif choice == "2":
        atm = float(input("Enter the amount to deposit: "))
        deposit(atm)
        print (f"amount{atm} deposit successfully")
    elif choice == "3":
        atm = float(input("Enter the amount to withdraw: "))
        withdraw(atm)
    elif choice == "4":
        check_kyc()
    elif choice == "5":
        kyc_doc = {}
        n_doc = int(input("enter the number of document you want to add: "))
        for i  in range(n_doc):
            key = input("enter the document type: ")
            value = input("enter the document number: ")
            kyc_doc[key] = value 
        update_kyc(kyc_doc)
        print ("kyc udated")
    elif choice == "6":
        print("You are Quiting.have a nice day.")
        break
    else :
        print ("Invalid choice!!! Re-try ") 

print ("Thank you")