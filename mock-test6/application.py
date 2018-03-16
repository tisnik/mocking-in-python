class Application:

    def __init__(self):
        pass

    def method1(self):
        print("method1 called")
        return self.method2()

    def method2(self):
        print("method2 called")
        return "method 2"
