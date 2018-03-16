from unittest.mock import *

import application


def test1():
    print(application.function1())


@patch('application.function1', return_value=42)
def test2(mocked_function):
    print(application.function1())


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()
