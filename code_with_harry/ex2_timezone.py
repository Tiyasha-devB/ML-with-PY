import time
print(f'Time now is: {time.strftime('%H:%M:%S')}') #returns string 
hour = int(time.strftime("%H"))

if hour >= 00 and hour < 12 :
    print("Good Morning, Ma'am")
if hour >= 12 and hour < 16 :
    print("Good Afternoon, Ma'am")
if hour >= 16 and hour < 24 :
    print("Good Night, Ma'am")
   