class Agent:
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self.__clearance_level = clearance_level

    def report(self):
        print(f"Agent {self.code_name} reporting.\n"
              f"Clearance Level: {self.__clearance_level}")

    def get_clearance_level(self):
        return self.__clearance_level

    def set_clearance_level(self, level: int):
        if 1 <= level <= 5:
            self.__clearance_level = level



