import random
import time

Regame=True
while Regame:
    lis=["Rock","Paper","Scissor"]
    user=input("Give a sign,(Rock,Paper,Scissor):").capitalize()
    
    if user not in lis:
        print("Enter an valid sign to continue the game")
        continue
    
    machine=random.choice(lis)
    print(f"you choosed:{user}")
    time.sleep(2)
    print(f"Machine choosed:{machine}")
    
    
    if user==machine:
        time.sleep(1)
        print("Its a tie!")
    elif user=="Rock" and machine=="Scissor":
        time.sleep(1)
        print("You Win!")
    elif user=="Scissor" and machine=="Paper":
        time.sleep(1)
        print("You Win!")
    elif user=="Paper" and machine=="Rock":
        time.sleep(1)
        print("You Win!")
    else:
        time.sleep(1)
        print("You lose")
            
    Want_to_palyagain=input("Enter Yes to continue or else No:").lower()
    if Want_to_palyagain=="yes":
        Regame=True
    else:
        Regame=False
        
print("Thanks for playing!")




