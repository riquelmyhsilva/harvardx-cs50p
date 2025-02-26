def main():
    m = int(input("m:"))
    E = e_equals_mc2(m)

    print(E)


def e_equals_mc2(mass):
    c = 300000000
    E = mass * (c**2)
    return E


main()
