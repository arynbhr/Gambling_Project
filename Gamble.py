import random
import sys

def check_line(dict,i):
    return all(k==dict[i][0] for k in dict[i])
def gamble(balance,bet,lines):
    entity=["#","$","*","&"]
    check_var=0
    dict={
        0:["","",""],
        1:["","",""],
        2:["","",""]
    }
    for i in range(len(dict)):
        for j in range(len(dict)):
            dict[i][j]=random.choice(entity)
    for i in range(len(dict)):
        for j in range(3):
            print("|",dict[i][j]+" |",end="")
        print()
    for i in range(3):
        bool=check_line(dict,i)
        if bool==True:
            check_var+=1
    if check_var>=lines:
        print("\n🥳Congrats, You won.")
        return balance + (bet*lines)
    else:
        print("\n😢Sorry, You lost.")
        return balance - (bet*lines)
                                   
def bet_amt():
    while True:
        bet=input("\nEnter your bet amt : $")
        if bet.isdigit()==True:
            if int(bet)==0:
                print("\nBet amount should be > 0.")
                continue
            else:
                break    
        else:
            print("\nBet amount should be in digits.")
            continue
    return int(bet)
def cst_deposit():
    while True:
        deposit=input("Enter your deposit amt : $")
        if deposit.isdigit()==True:
            if int(deposit)<=0:
                print("Deposit amount should be > 0.")
                continue
            else:
                break    
        else:
            print("Deposit amount should be in digits.")
            continue
    return int(deposit)
def game():
    balance=cst_deposit()
    while True:
        if balance>0:
            print(f"\nYour balance is ${balance}")
            choice=input("\nDo you wantt to bet (yes) or q for quit :")
            if choice.lower()=="yes":
                bet=bet_amt()
                lines=int(input("\n\nEnter the number of lines you bet on (1-3) : "))
                if (bet*lines)<=balance:
                    balance=gamble(balance,bet,lines)
                else:
                    print(f"\nYour bet amount {bet} and lines {lines} is total {bet*lines} which is higher than {balance}. Try with lower amount.")
                    continue    
            elif choice.lower()=="q":
                break
            else:
                continue
        else:
            print("\nSorry,you can't bet. You are out of balance.")
            choose=input("Do you want to add more balance (add) or q for exit :")
            if choose.lower()=="add":
                game()
            elif choose.lower()=="q":
                sys.exit()        
    print(f"\n\nYour balance is ${balance}")
game()    