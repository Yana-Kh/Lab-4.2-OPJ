#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Дополнительно к требуемым в заданиях операциям перегрузить операцию
индексирования []. Максимально возможный размер списка задать константой.
В отдельном поле size должно храниться максимальное для данного объекта
количество элементов списка; реализовать метод size(), возвращающий
установленную длину. Если количество элементов списка изменяется во
время работы, определить в классе поле count. Первоначальные значения
size и count устанавливаются конструктором. В тех задачах, где
возможно, реализовать конструктор инициализации строкой.

Вариан 29(8). Реализовать класс Money, используя для представления суммы денег
список словарей.Словарь имеет два ключа: номинал купюры и количество купюр
данного достоинства. Номиналы представить как строку. Элемент списка словарей
с меньшим индексом содержит меньший номинал.
"""


class Money:

    MAX_SIZE = 10

    def __init__(self, money_list):
        self.money_list = []
        self.size = Money.MAX_SIZE
        self.count = 0

        if isinstance(money_list, str):
            list_for_dir = money_list.split(", ")
            for d in list_for_dir:
                temp = d.split(": ")
                if temp[0].isnumeric() and temp[1].isnumeric():
                    nominal = int(temp[0])
                    number = int(temp[1])
                    if self.count < self.size:
                        self.money_list.append({"номинал": str(nominal), "количество": number})
                        self.count += 1

            self.money_list = sorted(self.money_list, key=lambda x: int(x['номинал']))

    def summ(self):
        total_sum = 0
        for temp in self.money_list:
            total_sum += int(temp["номинал"]) * temp["количество"]
        print(f"Общая сумма: {total_sum}")

    def add(self, nominal, number):
        for temp in self.money_list:
            if str(nominal) in temp.keys():
                temp["количество"] += number
            if self.count < self.size:
                self.money_list.append({"номинал": str(nominal), "количество": number})
                self.count += 1
                self.money_list = sorted(self.money_list, key=lambda x: int(x["номинал"]))
            else:
                print("Список заполнен")

    def remove(self, nominal, number):
        for temp in self.money_list:
            if str(nominal) in temp.keys():
                if number <= temp["количество"]:
                    temp["количество"] -= number
                    if temp["количество"] == 0:
                        self.money_list.remove(temp)
                        self.count -= 1
                else:
                   print("Вычитаемая сумма больше сществующей ")

    def __getitem__(self, index):
        return self.money_list[index]

    def ssize(self):
        print(f"Размер словаря: {self.count}")


if __name__ == '__main__':
    # инициализация объекта класса с помощью строки
    money1 = Money("100: 10, 50: 5, 10: 20, 200: 1")
    print(money1.ssize())
    print(money1.summ())
    money1.add(1000, 5)
    print(money1.ssize())
    print(money1.summ())
    money1.remove(10, 1)
    print(money1.ssize())
    print(money1.summ())
    print(money1[0])
    print(money1[3])
