#GROUP MEMBERS - SAI NARU, JEREME YANG

"""Build a command-line scientific calculator including 7 arithmetic operations"""
import math

#Takes in total previous calculations sums and number of previous calculations, and prints sum, number, and average of these data (in other words the display data operation)
def print_display_data(sum_calculations,num_of_calculations):
    print("\nSum of calculations: ", round(sum_calculations, 2))
    print("Number of calculations: ", round(num_of_calculations))
    print("Average of calculations: ", round(sum_calculations / num_of_calculations, 2), "\n")

#takes in user's input and either converts to previous current result if user types 'RESULT', or converts user input to float
def transform_operand(current_operand,prev):
    if(current_operand == 'RESULT'):
        return prev
    else:
        return float(current_operand)

#function that prints calculator menu
def menu():
    print("Calculator Menu\n--------------- \n0. Exit Program \n1. Addition \n2. "
          "Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation "
          "\n6. Logarithm \n7. Display Average\n")

#fucntion that takes in two user input numbers and applies calculator menu option based on menu selection and returns current result
def do_math(operand_one,operand_two,menu_selection):
    if menu_selection == 1:
        return (operand_two + operand_one)
    elif menu_selection == 2:
        return (operand_one - operand_two)
    elif menu_selection == 3:
        return (operand_one * operand_two)
    elif menu_selection == 4:
        return (operand_one / operand_two)
    elif menu_selection == 5:
        return (operand_one ** operand_two)
    elif menu_selection == 6:
        return (math.log(operand_two, operand_one))

#Based on the flag, program either prints the current result and menue,or if 7/out of bound number is inputed then no table is printed
def check_print_table(flag,solution):
    if(flag):
        print("Current Result:", solution, '\n')
        menu()
        return True
    return False

if __name__ == "__main__":
    menu_selection = 1
    sum_calculations = 0
    num_of_calculations = 0
    solution = 0.0

    #Flag checks weither to print menue or not based on if the previous menu input was either a 7 or out of bounds number
    flag = True
    prev = 0
    while(menu_selection != 0):
        if(check_print_table(flag,solution)):
            prev = solution
            solution = 0

        menu_selection = float(input("Enter Menu Selection: "))

        if(menu_selection == 0):
            break
        elif(menu_selection < 0 or menu_selection > 7):
            print("\nError: Invalid selection!\n")
            flag = False
        elif(menu_selection == 7):
            if(num_of_calculations > 0):
                print_display_data(sum_calculations,num_of_calculations)
            else:
                print("\nError: No calculations yet to average!\n")
            flag = False
        else:
            flag = True
            operand_one = transform_operand(input("Enter first operand: "),prev)
            operand_two = transform_operand(input("Enter second operand: "),prev)
            print()
            solution = do_math(operand_one,operand_two,menu_selection)
            sum_calculations += solution
            num_of_calculations += 1

    print()
    print("Thanks for using this calculator. Goodbye! ")
