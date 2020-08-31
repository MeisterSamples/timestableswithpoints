#!/opt/anaconda3/bin/python

# this quiz counts up the wrong/right answers and totals them at the end
import random
q=0
def randomtimes():
    total =0
    for q in range(required):
        q=q+1

        first = random.randint(1,12)
        second = random.randint(1,12)
        print()
        print ('What is '+str(first) +' multiplied by '+str(second)+('?'))

        print()
        result = int((first*second))
        answer=int(input())
        if answer==result:
            print('✓')
            total= total+1
        else:
            print("""ಠ_ಠ""")

    print()
    print('You got '+str(total)+' out of '+ str(q))
    print()
    percentage = total/q *100
    roundpercentange = round(percentage,2)
    print('This means you got ' + str(roundpercentange)+'%')

    
def giventimes():
    total =0
    for q in range(required):
        q=q+1
        first = random.randint(1,12)
        second = int(choice)
        print()
        print ('What is '+str(first) +' multiplied by '+str(second)+('?'))
        print()
        result = int((first*second))
        answer=int(input())
        if answer==result:
            total= total+1
            print('✓')
        else:
            print("""ಠ_ಠ""")
    print()
    print('You got '+str(total)+' out of '+ str(q))
    print()
    percentage = total/q *100
    percentage = total/q *100
    roundpercentange = round(percentage,2)
    print('This means you got ' + str(roundpercentange)+'%')


print('How many questions do you want?')
print()

required = int(input())
print()
print('Which times table do you want to be tested on? Enter a number or type "I feel lucky"')
print()
choice= input()



if choice == 'I feel lucky':
   randomtimes()
else:
   giventimes()


    




    
