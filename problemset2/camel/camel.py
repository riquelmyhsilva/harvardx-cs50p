def main():

    camel_to_snake(input("camelCase: "))


def camel_to_snake(camel):

    snake = ""

    for c in camel:
        if c.isupper():
            snake += "_"
            snake += c.lower()
        else:
            snake += c

    print("snake_case: " + snake)

main()
