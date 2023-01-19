from typing import Union
import doctest


class Speed:
    def __init__(self, distance: Union[int, float], time: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Скорость движения"
        :param distance: Пройденная дистанция
        :param time: Время, за которое пройдена дистанция
        Примеры:
        >>> speed = Speed(50, 5)  # инициализация экземпляра класса
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Пройденная дистанция должна быть типа int или float")
        if distance < 0:
            raise ValueError("Пройденная дистанция не может быть отрицательным числом")
        self.distance = distance

        if not isinstance(time, (int, float)):
            raise TypeError("Время должно быть типа int или float")
        if time < 0:
            raise ValueError("Время не может быть отрицательным числом")
        self.time = time

    def find_speed(self) -> int:
        """
        Функция, которая определяет скорость движения
        :return: Скорость движения
        Примеры:
        >>> speed = Speed(50, 5)
        >>> speed.find_speed()
        10
        """
        if self.time == 0:
            raise ValueError("На ноль делить нельзя!")
        return self.distance // self.time

    def check_speed(self, limit: int) -> bool:
        """
        Функция, которая проверяет превышение скорости
        :param limit: Ограничение скорости
        :return: Превышена ли скорость
        Примеры:
        >>> speed = Speed(50, 5)
        >>> speed.check_speed(40)
        True
        """
        if self.distance // self.time > limit:
            raise ValueError("Скорость превышает ограничение {limit}")
        else:
            return True


if __name__ == "__main__":
    doctest.testmod()
