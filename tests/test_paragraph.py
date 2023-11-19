import unittest
# noinspection PyUnresolvedReferences
from dz_5_unit.note.paragraph import Paragraph
from datetime import datetime


class TestParagraph(unittest.TestCase):
    def setUp(self):
        self.quiz_date = datetime.today().replace(microsecond=0)
        self.paragraph = Paragraph("Test Head", "Test Content")

    def tearDown(self):
        del self.quiz_date
        del self.paragraph

    def test_get_date(self):
        self.assertEqual(self.paragraph.get_date(), str(self.quiz_date))

    def test_get_head(self):
        self.assertEqual(self.paragraph.get_head(), "Test Head")

    def test_get_content(self):
        self.assertEqual(self.paragraph.get_content(), "Test Content")

    def test_get_all(self):
        self.assertEqual(self.paragraph.get_all(), (str(self.quiz_date), "Test Head", "Test Content"))
