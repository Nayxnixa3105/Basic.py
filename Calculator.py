print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Floor_divide")

choice=input("Enter your choice:")
num_1 = float(input("Enter the first number:"))
num_2 = float(input("Enter the second number"))

if choice == "1":
    print(num_1, '+' ,num_2, '=',(num_1+num_2))
elif choice == "2":
    print(num_1, '-', num_2, '=',(num_1-num_2))

elif choice =="3":
    print(num_1, '*', num_2, '=',(num_1*num_2))

elif choice =="4":
    if num_2 =='0.0':
        print("Divide by 0 Error")
    print(num_1, '/', num_2, '=',(num_1/num_2))

elif choice == "5":
    print(num_1, '//', num_2, '=',(num_1//num_2))

else:
    print("invalid choice")