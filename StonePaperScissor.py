import random
computer_choice=['Stone','Paper','Scissor']
d =0
p=0
i=int(0)
name=input("Enter Your Name-")
matches=int(input("Enter Rounds-"))


while i<=matches-1:
     command = input("Enter Stone/Paper/Scissor-")
     t = random.choice(computer_choice)
     if t == command :
        i+=1
        print("Tie")
     elif command=="Stone" and t=="Paper":
       d+=1
       i+=1
       print("Computer Win")
     elif command=="Scissor" and t=="Stone":
         d+=1
         i+=1
         print("Computer Win")
     elif command=="Paper" and t=="Scissor":
         d+=1
         i+=1
         print("Computer Win")
     elif command == "Stone" and t == "Scissor":
         p+= 1
         i+=1
         print(name +"-Win")
     elif command == "Scissor" and t == "Paper":
        p+= 1
        i+=1
        print(name +"-Win")
     elif command == "Paper" and t == "Stone":
         p+= 1
         i+=1
         print(name+ "-Win")
     elif command=="Quit" or command=="quit":
        break


print("Computer Score:"+str(d))
print("Player Score:"+str(p))
if d>p:
     print("You Lose Computer Win")
elif d==p:
     print("Draw Match")
else:
     print("You Win the All Rounds-"+name)
