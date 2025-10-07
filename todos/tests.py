from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="first todo",
            body="a body here",
        )

    def test_title_content(self):
        self.assertEqual(self.todo.title, "first todo")

    def test_body_content(self):
        self.assertEqual(self.todo.body, "a body here")
