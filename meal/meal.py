def main():

    user_input = str(input("What time is it? "))

    time = convert(user_input)

    meal(time)


def convert(time):

    time = time.replace(":"," ")
    time = time.replace(".", "")
    time = time.split(" ")

    h = float(time[0])
    m = float(time[1]) / 60

    time.pop(0)
    time.pop(0)

    time.insert(0, h + m)

    return time


def meal(time):

    h = time[0]

    if h >= 7 and h <= 8:
        print("breakfast time")
    elif h >= 7 and h <= 8 and "am" in time:
        print("breakfast time")
    elif h >= 12 and h <= 13:
        print("lunch time")
    elif h >= 12 and h <= 12.9 or h == 1 and "pm" in time:
        print("lunch time")
    elif h >= 18 and h <= 19:
        print("dinner time")
    elif h >= 6 and h <= 7 and "pm" in time:
        print("dinner time")
    else:
        None


if __name__ == "__main__":
    main()
