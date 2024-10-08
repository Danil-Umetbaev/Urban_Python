first = int(input("Enter the number: "))
second = int(input("Enter the number: "))
third = int(input("Enter the number: "))
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(1)
