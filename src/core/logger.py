class Logger:

    @staticmethod
    def info(*args):
        print(*args)
        pass

    @staticmethod
    def error(*args):
        print("ERROR: ", end="")
        print(*args)
        pass

    @staticmethod
    def debug(*args):
        print("Debug - ", end="")
        print(*args)
        pass

