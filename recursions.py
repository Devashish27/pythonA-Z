# def print2(str1):
#     print2(str1)
#     print("This is " + str1)
#
#
# print2("VW Polo")


# factorial code...!
def factorial_iterative(n):
    """
      :param n: Integer
      :return: n * n-1 * n-2 * n-3...1
      """

    fac = 1

    for i in range(n):
        fac = fac * (i + 1)

    return fac


def factorial_recursive(n):
    """
      :param n: Integer
      :return: n * n-1 * n-2 * n-3...1
      """

    if n == 1:
        return 1

    else:
        return n * factorial_recursive(n - 1)


# Fibonacci series...!
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter a number!\n"))
# print("Factorial Using Iterative Method: ", factorial_iterative(number))
# print("Factorial Using Recursive Method: ", factorial_recursive(number))
print("Fibonacci Numbers series are: ", fibonacci(number))
