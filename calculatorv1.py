import math
# Function to solve quadratic equations i actually hate these so much omg 
def solve_quadratic():
    a = float(input("Please enter your value of a: "))
    b = float(input("Please enter your value of b: "))
    c = float(input("Please enter your value of c: "))

    if a == 0:
        print("That isn't a quadratic equation, sorry man.")
        return

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("No real roots, my dude. Can't solve that one")
        return

    xone = (-b + math.sqrt(discriminant)) / (2*a)
    xtwo = (-b - math.sqrt(discriminant)) / (2*a)

    print("Value of x1:", xone)
    print("Value of x2:", xtwo)
# Function to solve linear equations this was actually so stupid i spent so long wondering how i solve quadratics so i could understand the logic its kinda funny actually
def solve_linear():
    a = float(input("Please enter your value of a: "))
    b = float(input("Please enter your value of b: "))

    if a == 0:
        print("Sorry, that isn't a linear equation! oopsies.")
    else:
        x = -b / a
        print("Value of x:", x)

# Main function to pick which type to solve (finallY)
def main():
    question_type = input("What type of equation would you like to solve? (linear/quadratic): ").strip().lower()

    if question_type == "quadratic":
        solve_quadratic()
    elif question_type == "linear":
        solve_linear()
    else:
        print("Um sorry, can't solve that one.")
main()
