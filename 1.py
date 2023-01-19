import doctest


class Notebook:
    def __init__(self, page_number: int, page_used: int):
        """
        Создание и подготовка к работе объекта "Тетрадь"
        :param page_number: Количество страниц в тетради
        :param page_used: Количество использованных страниц
        Примеры:
        >>> notebook = Notebook(24, 3)  # инициализация экземпляра класса
        """
        if not isinstance(page_number, int):
            raise TypeError("Количество страниц должно быть типа int")
        if page_number <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.page_number = page_number

        if not isinstance(page_used, int):
            raise TypeError("Количество страниц должно быть типа int")
        if page_used < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")
        self.page_used = page_used

    def is_empty_notebook(self) -> bool:
        """
        Функция, которая проверяет является ли тетрадь пустой
        :return: Является ли тетрадь пустой
        Примеры:
        >>> notebook = Notebook(24, 3)
        >>> notebook.is_empty_notebook()
        True
        """
        if self.page_used > 0:
            return True

    def write(self, page: int) -> None:
        """
        Функция записи количества использованных страниц
        :param page: Количество использованных страниц
        :raise ValueError: Если количество использованных страниц превышает количество
        свободных страниц, то вызываем ошибку
        Примеры:
        >>> notebook = Notebook(24, 3)
        >>> notebook.write(4)
        """
        if self.page_used + page > self.page_number:
            raise ValueError("Количество страниц не может быть больше {self.page_number}")
        self.page_used += page


if __name__ == "__main__":
    doctest.testmod()
