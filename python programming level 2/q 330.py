y=int(input("Enter year to be checked:"))
if(y%4==0 and y%100!=0 or y%400==0):
        print("The year is a leap year!")
else:
        print("The year isn't a leap year!")
