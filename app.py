from calc_fun import do_addition, do_subtraction, do_division
from multiply import do_multiplication
from area import calculate_area_rectangle
def main():
    print('Welcome to the calculator app')
    print('''\nSelect the cunction from the given options
          1. Add
          2. Subtract
          3. Multiply
          4.Division
          ''')
    
    user_input = str(input('select the input'))
    a = int(input('Value of A'))
    b = int(input('Value of B'))

    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_subtraction(a,b)

    elif user_input == "3":
        result = do_multiplication(a,b)

    elif user_input == '4':
        result = do_division(a,b)

    

    

    print('Result: ', result)

if __name__ == '__main__':
    main()

    
    
