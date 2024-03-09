class Human:
    default_name = "Данил"
    default_age = 20
    def __init__(self, name, age):
        if name:
            self.name = name
        else:
            self.name = Human.default_name
        if age:
            self.age = age
        else:
            self.age = Human.default_name
        self.__money = 0
        self.__house = None

    def info(self):
        print("Человек:", self.name, "; возраст:", self.age, "; счёт:", self.__money, "; дом:", self.__house)

    @staticmethod
    def default_info():
        print("Стандартный человек:", Human.default_name, Human.default_age)

    def __make_deal(self, house):
            self.__house = house
            self.__money -= house._price

    def earn_money(self, cash):
        self.__money += cash
        print(f"Человек {self.name} получил {cash} денег")

    def buy_house(self, house):
        if self.__money < house._price:
            print(f"Человеку {self.name} не хватает денег(")
        else:
            print(f"Человек {self.name} купил дом!")
            self.__make_deal(house)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


Human.default_info()
human1 = Human("Стас", 17)
human1.info()
small_house = SmallHouse(10000)
human1.buy_house(small_house)
human1.earn_money(100000)
human1.buy_house(small_house)