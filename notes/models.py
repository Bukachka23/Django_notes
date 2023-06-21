from django.db import models

# Define a Category model
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        # The plural name for Category instances
        verbose_name_plural = 'Category'
        # The default ordering for Category instances (by created date)
        ordering = ['created']

    def __str__(self):
        return self.title

# Define a Note model
class Note(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name_plural = 'Заметки'
        ordering = ['-created']

    def __str__(self):
        return self.title

