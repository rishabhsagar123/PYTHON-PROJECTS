
import tkinter.messagebox as mb
mb.showinfo("Game","Lets Start the Game")






class game:
    def __init__(self,name):
        self.name=name
        
        
print('Hello Welcome to the game there are 2 questions in this game')
ans=input('Enter The answer of Following Questions and Play(yes/No):')
score=0
total_q=2

if ans.lower()=='yes':
    ans=input('1,what is the best programming language?:')
    if ans.lower()=='python':
        score+=1
        p2=game("Correct")
        print(p2.name)
        ans=input('2,What is your name?:')
        if ans.lower()=='rishabh':
            score+=1
            print('Correct')
            print('Your Score are:',score)
            t=(score/2)*100
            print("You get the Percentage:", t)
            print("Total Questions are:",total_q)
            p1=game("Hurray You Win!!!")
            print(p1.name)
            


    else :
        score-=1
        print('Incorrect')
        print('Your Score is:',score)
        t=(score/2)*100
        print('You get the Percentage:',t)
        print('Total questions are',total_q)
        p3=game("You Lose")
        print(p3.name)
        
        
        


if ans.lower()=='no':
    ans=input('3,You want to quit the game(yes/no)?:')
    if ans.lower()=='yes':
        print('Your Score are:',score)
        t=(score/2)*100
        print("You get the Percentage:", t)
        print("Total questions are:",total_q)

    else :
        mb.showinfo("Game","Restart the Game")
        
        


        
    
