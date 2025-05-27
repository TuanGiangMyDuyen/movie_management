import random

class RandomCode:

    @staticmethod
    def random_code():
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        return str(code)