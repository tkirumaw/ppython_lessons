def emobilis():
    print("eMobilis is a tech institute.")
#emobilis()
def addtwonum():
    num_1=int(input("Enter first number: "))
    num_2=int(input("Enter second number: "))
    print(f"The sum of {num_1} and {num_2} is {num_1+num_2}")
#addtwonum()

def calc_bmi():
    weight=float(input("Enter your weight: "))
    height=float(input("Enter your height in metres: "))
    bmi=float(weight)/(height**2)

    if bmi<18.5:
        print("You are underweight")
    elif bmi>18.5 and bmi<24.9:
        print("You are healthy")
    elif bmi>24.9 and bmi<29.9:
        print("You are overweight")
    elif bmi>=30:
        print("You are obese")
calc_bmi()