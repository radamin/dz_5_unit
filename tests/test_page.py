import unittest
# noinspection PyUnresolvedReferences
from dz_5_unit.note.page import Page


class TestPage(unittest.TestCase):
    def setUp(self):
        self.page = Page("Head 1", "Content 1")
        for i in range(2, 6):
            self.page.write(f"Head {i}", f"Content {i}")

    def tearDown(self):
        del self.page

    # unit tests
    def test_search_private(self):
        search = self.page._Page__search("Head 1")
        self.assertEqual(search, self.page.page[0])

    def test_not_search_private(self):
        search = self.page._Page__search("Head 7")
        self.assertIsNone(search)

    def test_read_paragraph(self):
        print("\n__test_read_paragraph__now data/time Head 3 Content 3")
        self.page.read_paragraph("Head 3")
        print("_" * 30)

    def test_read_page(self):
        print("\n__test_read_page__5 paragraphs")
        self.page.read_page()
        print("_" * 30)

    def test_write(self):
        # добавили запись на страницу
        self.page.write("head TWO", "content TWO")

        # убедились что число записей увеличилось на один
        self.assertEqual(len(self.page.page), 6)

        # убедились что содержимое последней записи на странице соответствует заданному
        page_test = (self.page.page[-1].get_head(), self.page.page[-1].get_content())
        self.assertEqual(page_test, ("head TWO", "content TWO"))

    def test_rewrite_content(self):
        self.page.rewrite_content("Head 2", "new content")

        self.assertEqual(self.page.page[1].get_content(), "new content")

    def test_rewrite_head(self):
        self.page.rewrite_head("Head 4", "NEW head")

        self.assertEqual(self.page.page[3].get_head(), "NEW head")

    def test_del_page(self):
        self.page.del_page("Head 3")

        # убедились что число записей уменьшилось на один
        self.assertEqual(len(self.page.page), 4)

        # убедились что содержимое третьей записи теперь соответствует бывшей четвертой
        page_test = (self.page.page[2].get_head(), self.page.page[2].get_content())
        self.assertEqual(page_test, ("Head 4", "Content 4"))

    # Интеграционные тесты
    def test_write_and_del(self):
        self.page.write("new", "test")
        self.page.write("new2", "text2")
        self.page.del_page("new")
        self.page.del_page("new")
        self.page.write("new3", "text3")
        self.page.del_page("new3")

        self.assertEqual(len(self.page.page), 6)

        # убедились что содержимое последней записи теперь соответствует второй добавленной
        page_test = (self.page.page[-1].get_head(), self.page.page[-1].get_content())
        self.assertEqual(page_test, ("new2", "text2"))

    def test_read_page_and_rewrites(self):
        print("\n__test_read_page_and_rewrites___change 1 and two paragraphs")
        self.page.read_page()
        self.page.rewrite_content("Head 1", "python")
        self.page.rewrite_head("Head 2", " rust")
        print()
        self.page.read_page()
        print("_" * 30)

    # Сквозные тесты
    def test_complete_workflow(self):
        for i in range(4):
            self.page.del_page(f"Head {i}")

        self.page.write("rust", "pytho")
        self.page.rewrite_content("rust", "python")
        self.page.rewrite_head("Head 3", "coverage")
        self.page.read_paragraph("python")
        self.page.read_page()

        self.assertEqual(len(self.page.page), 3)
