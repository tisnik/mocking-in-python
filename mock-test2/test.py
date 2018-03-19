from unittest.mock import *

import application


def test1():
    print(application.function1())


@patch('application.function1', return_value=42)
def test2(mocked_function):
    print(application.function1())


def side_effect_handler():
    print("side_effect function called")
    return -1


@patch('application.function1', side_effect=side_effect_handler)
def test3(mocked_function):
    print(application.function1())


@patch('application.function1', return_value=42, side_effect=side_effect_handler)
def test4(mocked_function):
    print(application.function1())


def side_effect_handler_2():
    print("side_effect function called")
    return DEFAULT


@patch('application.function1', return_value=42, side_effect=side_effect_handler_2)
def test5(mocked_function):
    print(application.function1())


if __name__ == '__main__':
    print("*** test1 ***")
    test1()
    print()

    print("*** test2 ***")
    test2()
    print()

    print("*** test3 ***")
    test3()
    print()

    print("*** test4 ***")
    test4()
    print()

    print("*** test5 ***")
    test5()
    print()

    print("*** test1 ***")
    test1()
    print()
