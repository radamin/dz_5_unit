from datetime import datetime


class Paragraph:
    def __init__(self,  head: str, content: str):
        self.__data = datetime.today().replace(microsecond=0)
        self.__head = head
        self.__content = content

    # Геттеры
    def get_date(self) -> str:
        return str(self.__data)

    def get_head(self) -> str:
        return self.__head

    def get_content(self) -> str:
        return self.__content

    def get_all(self) -> tuple[str, str, str]:
        return self.get_date(), self.get_head(), self.get_content()

    # Сеттеры
    def set_head(self, head) -> None:
        self.__head = head

    def set_content(self, content) -> None:
        self.__content = content
