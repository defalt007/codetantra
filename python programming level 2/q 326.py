n=int(input("Enter a number:"))
sum = 0
for digit in str(n):
        sum += int(digit)
print(f"The total sum of digits is: {sum}")
