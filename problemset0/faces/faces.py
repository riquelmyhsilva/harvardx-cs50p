def main():
    converted_text = convert(str(input("--> ")))
    print(converted_text)


def convert(text):
    if ":)" in text or ":(" in text:
        text = text.replace(":(", "🙁")
        text = text.replace(":)", "🙂")
        return text


main()
