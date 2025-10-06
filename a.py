while True:
    print ("1 Add")
    print ("2 sub")
    print ("3 multi")
    print ("4 div")
    print ("5 exit")
    a = input("Enter your choice (1-5): ")
    
    if a == '5':
        print ("Thank you for using the calculator! Goodbye!")
        break
    if a not in ['1','2','3','4']:
        print('please enter a valid input')
        continue
    try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
    except ValueError:
            print("Error: Please enter valid numbers!")
            continue
    if a == '1':
            result = num1 + num2
            print(f"*Result: {num1 + num2}")
    elif a == '2':
            result = num1 - num2
            print(f"*Result: {num1 - num2}")
    elif a == '3':
          result = num1 * num1
          print(f"*Result: {num1 * num2}")
    elif a == '4':
        if num2 == 0:
                print('Error: zerodivision error')
        else :
              print(f'*Result: {num1/num2}')
        