lr = int(input("Enter the lower limit for the range:"))
ul = int(input("Enter the upper limit for the range:"))
for num in range(lr,ul+1):
        if num % 2 != 0:
                print(num, end = "\n")
