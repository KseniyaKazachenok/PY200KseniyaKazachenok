import doctest


class Chameleon:
    def __init__(self, colour: str, size: int):
        """
        Создание и подготовка к работе объекта "Хамелеон"
        :param colour: Цвет хамелеона
        :param size: Размер хамелеона в сантиметрах
        Примеры:
        >>> chameleon = Chameleon('Зеленый', 15)  # инициализация экземпляра класса
        """
        if not isinstance(colour, str):
            raise TypeError("Цвет хамелеона должен быть типа str")
        if colour not in ['Синий', 'Зеленый', 'Красный', 'Желтый']:
            raise ValueError("Цвет хамелеона должен быть из списка: Синий, Зеленый, Красный, Желтый")
        self.colour = colour

        if not isinstance(size, int):
            raise TypeError("Размер хамелеона должен быть типа int")
        if size <= 0:
            raise ValueError("Размер хамелеона должен быть положительным числом")
        self.size = size

    def change_colour(self, new_colour: str):
        """
        Функция, которая меняет цвет хамелеона
        :return: Новый цвет хамелеона
        Примеры:
        >>> chameleon = Chameleon('Зеленый', 15)
        >>> chameleon.change_colour('Синий')
        'Синий'
        """
        if new_colour in ['Синий', 'Зеленый', 'Красный', 'Желтый']:
            self.colour = new_colour
            return self.colour
        else:
            raise ValueError("Цвет хамелеона должен быть из списка: Синий, Зеленый, Красный, Желтый")

    def size_mm(self) -> int:
        """
        Функция, которая выражает размер хамелеона в милиметрах
        :return: Размер хамелеона в милиметрах
        Примеры:
        >>> chameleon = Chameleon('Зеленый', 15)
        >>> chameleon.size_mm()
        150
        """
        return self.size * 10


if __name__ == "__main__":
    doctest.testmod()
