a=float(input("Enter marks of the first subject: "))
b=float(input("Enter marks of the second subject: "))
c=float(input("Enter marks of the third subject: "))
d=float(input("Enter marks of the fourth subject: "))
e=float(input("Enter marks of the fifth subject: "))
avg=(a+b+c+d+e)/5
if(avg>=95):        
        print("Grade: A") 
elif(avg>=80 and avg<90):        
        print("Grade: B")
elif(avg>=70 and avg<80):        
        print("Grade: C")
elif(avg>=60 and avg<70):        
        print("Grade: D")
else:        
        print("Grade: F")
