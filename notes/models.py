from django.db import models

# Create your models here.
class Note(models.Model):
    """Model representing a bulletin board post.
    Fields:
    - title: CharField for the post title with a maximum length of 255
    characters.
    - content: TextField for the post content.
    - created_at: DateTimeField set to the current date and time when the
    post is created.
    Relationships:
    - author: ForeignKey representing the author of the post.
    Methods:
    - __str__: Returns a string representation of the post, showing the
    title.
    :param models.Model: Django's base model class.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title