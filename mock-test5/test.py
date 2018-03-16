from unittest.mock import *

import application


def test1():
    print("function1 returns: {v}".format(v=application.function1()))


@patch('application.function2', return_value=42)
def test2(mocked_function):
    print("mocked function called: {c}".format(c=mocked_function.called))
    print("function1 returns: {v}".format(v=application.function1()))
    print("mocked function called: {c}".format(c=mocked_function.called))


def side_effect_handler():
    print("side_effect_handler function called")
    return -1


@patch('application.function2', side_effect=side_effect_handler)
def test3(mocked_function):
    print("mocked function called: {c}".format(c=mocked_function.called))
    print("function1 returns: {v}".format(v=application.function1()))
    print("mocked function called: {c}".format(c=mocked_function.called))


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()

    test3()
    print()
