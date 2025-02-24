def main():

    interpreter(str(input("Expression: ")))


def interpreter(expression):

    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/" and z != 0:
        print(x / z)
    else:
        print("It's wrong")

main()
