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
    print("mocked function called: {c}".format(c=mocked_function.called))
    print(application.function1())
    print("mocked function called: {c}".format(c=mocked_function.called))


@patch('application.function1', return_value=42, side_effect=side_effect_handler)
def test4(mocked_function):
    print(application.function1())


def side_effect_handler_2():
    print("side_effect function called")
    return DEFAULT


@patch('application.function1', return_value=42, side_effect=side_effect_handler_2)
def test5(mocked_function):
    print("mocked function called: {c}".format(c=mocked_function.called))
    print(application.function1())
    print("mocked function called: {c}".format(c=mocked_function.called))


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()

    test3()
    print()

    test4()
    print()

    test5()
    print()
