
from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name, count):
        """(<название>, <количество>)  - увеличивает запас items"""
        pass

    @abstractmethod
    def remove(self, name, count):
        """(<название>, <количество>) - уменьшает запас items"""
        pass

    @abstractmethod
    def get_free_space(self):
        """вернуть количество свободных мест"""
        pass

    @abstractmethod
    def get_items(self):
        """возвращает сожержание склада в словаре {товар: количество}"""
        pass

    @abstractmethod
    def get_unique_items_count(self):
        """возвращает количество уникальных товаров."""
        pass


class Store(Storage):

    def __init__(self, items: dict, capacity: int):
        super().__init__(items, capacity)
        self._capacity = 100

    def add(self, name, count):
        """(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity"""
        if sum(self._items.values()) + count <= self._capacity:
            self._items[name] = self._items.get(name, 0) + count
            return f"на складе хранится: {self._items}"
        return f"склад переполнен"

    def remove(self, name, count):
        """(<название>, <количество>) - уменьшает запас items"""
        if self._items.get(name, 0) - count < 0:
            return f"Товара не хватает"
        self._items[name] = self._items.get(name, 0) - count
        return f"на складе осталось: {self._items}"


    def get_free_space(self):
        """вернуть количество свободных мест"""
        return self._capacity - sum(self._items.values())

    def get_items(self):
        """возвращает сожержание склада в словаре {товар: количество}"""
        return self._items

    def get_unique_items_count(self):
        """возвращает количество уникальных товаров."""
        return len(self._items)

class Shop(Storage):

    def __init__(self, items, capacity):
        super().__init__(items, capacity)
        self._items = items
        self._capacity = 20

    def add(self, name, count):
        """(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity"""
        if sum(self._items.values()) + count <= self._capacity and len(self._items) < 5:
            self._items[name] = self._items.get(name, 0) + count
            return f"в магазине: {self._items}"
        return f"склад переполнен"

    def remove(self, name, count):
        """(<название>, <количество>) - уменьшает запас items но не ниже 0"""
        if self._items.get(name, 0) - count < 0:
            return f"Товара не хватает"
        self._items[name] = self._items.get(name, 0) - count
        return f"в магазине осталось: {self._items}"


    def get_free_space(self):
        """вернуть количество свободных мест"""
        return self._capacity - sum(self._items.values())

    def get_items(self):
        """возвращает сожержание склада в словаре {товар: количество}"""
        return self._items

    def get_unique_items_count(self):
        """возвращает количество уникальных товаров."""
        return len(self._items)

class Request:
    def __init__(self, data):
        data = data.lower().split(" ")
        self.from_ = data[4]  # откуда везем (строка)
        self.to = data[6]  # куда везем (строка)
        self.amount = int(data[1])  # кол-во
        self.product = data[2]  # продукт
