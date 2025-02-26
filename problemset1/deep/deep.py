def main():

    question = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

    deep_thought(question)


def deep_thought(answer):

    answer = answer.lower().strip()

    if answer in ("42", "forty two", "forty-two"):
        print("Yes")
    else:
        print("No")


main()
