Amount=0
while True:
    str=input("Enter Transaction (D/W): ")
    amt=int(input("Enter Transaction amount: "))
    if (str=='D' or str=='d'):
        Amount+=amt
        print("Net amount: ", Amount)
    elif (str=='W' or str=='w'):
        if (amt>Amount):
            print("Your Account have Low Amount")
        else:
            Amount-=amt
            print("Net amount: ", Amount)
    else:
        pass

    str1=input ("You want to continue (Y/N): ")
    if not (str1=="Y" or str1=="y"):
        break