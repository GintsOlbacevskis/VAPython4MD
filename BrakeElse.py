#Check if a number is prime
number = 30
is_prime = True

for i in range(2, int(number ** 0.5) +1):
    if number % i == 0:
        print(f"{number} dalīts ar {i}, nav pirmskaitlis")
        is_prime = False
        break
else:
    print(f"{number} ir pirmskaitlis")