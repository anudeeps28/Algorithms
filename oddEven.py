def oddOrEven(number):
    if number % 2 == 0:
        return "number is EVEN"
    else:
        return "number is ODD"

if __name__ == '__main__':
    number = 16
    print(oddOrEven(number))
