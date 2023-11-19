# noinspection PyUnresolvedReferences
from dz_5_unit.note.paragraph import Paragraph


class Page:
    def __init__(self, head: str, content: str):
        self.page: list = list()
        paragraph = Paragraph(head, content)
        self.page.append(paragraph)

    def __search(self, head: str) -> Paragraph:
        for path in self.page:
            if path.get_head() == head:
                return path

    def read_paragraph(self, head: str) -> None:
        search = self.__search(head)
        if search is not None:
            print(*self.__search(head).get_all())

    def read_page(self) -> None:
        for path in self.page:
            print(*path.get_all(), sep=" | ")

    def write(self, head: str, content: str) -> None:
        paragraph = Paragraph(head, content)
        self.page.append(paragraph)

    def rewrite_content(self, head: str, content: str) -> None:
        search = self.__search(head)
        if search is not None:
            self.__search(head).set_content(content)

    def rewrite_head(self, head: str, new_head: str) -> None:
        search = self.__search(head)
        if search is not None:
            self.__search(head).set_head(new_head)

    def del_page(self, head: str) -> None:
        search = self.__search(head)
        if search is not None:
            self.page.remove(search)
