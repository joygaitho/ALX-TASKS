import calculator
def main():
    try:
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
    except ValueError:
        print("invalid input: enter an integer")
    sum = calculator.add(num1, num2 )
    print(f"the sum of {num1} and {num2} is: {sum}")
    diff = calculator.subtract(num1, num2)
    print(f"the difference of {num1} and {num2} is: {diff}")
    product = calculator.multiply(num1, num2)
    print(f"the product of {num1} and {num2} is: {product}")
    quotient = calculator.divide(num1, num2)
    print(f"the quotient of {num1} and {num2} is: {quotient}")
if __name__ == "__main__":
    main()
