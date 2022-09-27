# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def card_hide(card):
#     return '*' * len(card[:-4]) + card[-4:]
#
# print(card_hide((input('Введите номер карты:'))))


# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# def palindrome(data):
#     data = data.replace(' ','').lower()
#     return 'Палиндром' if data == data[::-1] else 'Не палиндром'
#
# print(palindrome((input('Введите слово:'))))


# 3. Решите задачу

# 1. Создайте класс Tomato
class Tomato:
    # 2. Создайте статическое свойство states, которое будет содержать все стадии
    # созревания помидора
    states = {1: 'seed', 2: 'sprout', 3: 'flower', 4: 'green_tomato', 5: 'red_tomato'}

    # 3. Создайте метод __init__(), внутри которого будут определены два динамических
    # protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
    # значение из словаря states
    def __init__(self, index):
        self._index = index
        self._state = 1

    # 4. Создайте метод grow(), который будет переводить томат на следующую стадию
    # созревания
    def grow(self):
        if self._state < 5:
            self._state += 1
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

    # 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
    # последней стадии созревания)
    def is_ripe(self):
        if self._state == 5:
            return True
        return False


# Класс TomatoBush
# 1. Создайте класс TomatoBush
class TomatoBush:

    # 2. Определите метод __init__(), который будет принимать в качестве параметра
    # количество томатов и на его основе будет создавать список объектов класса
    # Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num)]

    # 3. Создайте метод grow_all(), который будет переводить все объекты из списка
    # томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
    # списка стали спелыми
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # 5. Создайте метод give_away_all(), который будет чистить список томатов после
    # сбора урожая
    def give_away_all(self):
        self.tomatoes = []


# Класс Gardener
# 1. Создайте класс Gardener
class Gardener:

    # 2. Создайте метод __init__(), внутри которого будут определены два динамических
    # свойства: 1) name - передается параметром, является публичным и 2) _plant -
    # принимает объект класса Tomato, является protected
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # 3. Создайте метод work(), который заставляет садовника работать, что позволяет
    # растению становиться более зрелым
    def work(self):
        print('working in progress..')
        self._plant.grow_all()

    # 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
    # садовник собирает урожай. Если нет - метод печатает предупреждение.

    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    # 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
    # по садоводству.
    @staticmethod
    def knowledge_base():
        print('Growing of potatoes consists of 5 stages:'
              ' 1 - seed,'
              ' 2 - sprout,'
              ' 3 - flower,'
              ' 4 - green tomato,'
              ' 5 - red tomato')


# Тесты:
# 1. Вызовите справку по садоводству
if __name__ == '__main__':
    Gardener.knowledge_base()

    # 2. Создайте объекты классов TomatoBush и Gardener
    great_tomato_bush = TomatoBush(10)
    gardener = Gardener('Andrey', great_tomato_bush)

    # 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
    gardener.work()

    # 4. Попробуйте собрать урожай
    gardener.harvest()

    # 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

    # 6. Соберите урожай
    gardener.harvest()
