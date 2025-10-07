import uuid

from django.db import models


class Todo(models.Model):
    """
    Represents a simple to-do item with a title and body content.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    
    title = models.CharField(
        max_length=200,
        help_text="Enter a short, descriptive title for the to-do item.",
    )
    
    body = models.TextField(
        help_text="Provide details or notes related to this to-do item.",
    )
    
    is_done = models.BooleanField(
        default=False,
        help_text="Indicates whether the todo item is completed."
    )


    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ["title"]

    def __str__(self):
        return self.title
