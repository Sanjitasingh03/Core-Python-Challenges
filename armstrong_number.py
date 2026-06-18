num = int(input("Enter a number: "))

order = len(str(num))
temp = num
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** order
    temp //= 10

if sum_of_powers == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")