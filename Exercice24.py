# asking the user to inter the value of n
n = int(input("Enter the value of n: "))

S = 0

# Loop to calculate the sum
for i in range(0, n + 1):
    S += 10**i

# the result of the sum
print(f"The sum S for n = {n} is: {S}")
