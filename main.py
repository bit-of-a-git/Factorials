def get_number():
    i = input("I will find the factorial of any positive integer you give me. Please enter an integer.\n")
    while not i.isdigit() or int(i) < 1:
        i = input("That is not a positive number. Please try again.\n")
    return int(i)


def compute_factorial(k):
    total = 1
    for number in range(1, k+1):
        total = total * number
    print(total)


j = get_number()
compute_factorial(j)
