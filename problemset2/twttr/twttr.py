def main():

    shorten(input("Input: "))


def shorten(prompt, vowels = ["a","e","i","o","u"], short_prompt = ""):

    for letter in prompt:
        if letter.lower() in vowels:
            None
        else:
            short_prompt += letter
    print("Output: " + short_prompt)

main()
