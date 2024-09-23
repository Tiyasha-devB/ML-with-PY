name = input("Enter your name: ")
print(f'''Lets play a KBC round, {name}!
Here is your First Question-''')

ques1 = "1.Who invented python?\n"
opt1 = ['Guido van Rossum',
            'Dennis Ritchie',
            'James Gosling']
print(ques1, "\nThe options are: ")
for op in opt1:
    print("#",op)
count = 0
ans1 = input("Enter your answer: ")
if (ans1 == 'Guido van Rossum' or ans1 == 'guido van rossum' or ans1 =='GUIDO VAN ROSSUM'):
    print("You win, round 1!")
    count+=1
else:
    print("You lost, better luck next time")

if count>0:
    print("\n You qualify for round 2: ")
