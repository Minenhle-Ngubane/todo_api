from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="First Todo",
            body="A body here",
            is_done=False,
        )

    def test_title_content(self):
        self.assertEqual(self.todo.title, "First Todo")

    def test_body_content(self):
        self.assertEqual(self.todo.body, "A body here")

    def test_is_done_default(self):
        self.assertFalse(self.todo.is_done)
