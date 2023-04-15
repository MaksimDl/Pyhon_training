class Human:
    sub_class = "человек разумный"  # переменная класса
    name: str
    age: int
    weight: float
    height: float

    def __init__(self, name: str, age: int, wight: float = 100, height: float = 170):
        self.name = name
        self.age = age
        self.weight = wight
        self.height = height

    def hello(self):
        return f'Тебя приветствует {self.name}'


kirill = Human('Stone', 38)
svetlana = Human('Света',18)

print(kirill.name)
print(kirill.height)
print(kirill.hello())


