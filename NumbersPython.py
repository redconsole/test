class NumberPython:
    num1 = 1
    num2 = 2

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def multiply(self):
        return self.num1 * self.num2

    def subtraction(self):
        return self.num1-self.num2

    @staticmethod
    def division():
        return 3/2

    @staticmethod
    def power_op():
        # self.division()
        return


def print_result(result):
    try:
        # print('Result is : {2:.4f}'.format(result))
        print(f'{result}')
    except IndexError:
        print('Error in formatting of float value')
    except TypeError:
        print('Error wrong method used')
    finally:
        print('Operation is completed')


def main_numbers():
    obj2 = NumberPython(100, 5)
    result = NumberPython.power_op()
    print_result(result)


main_numbers()



