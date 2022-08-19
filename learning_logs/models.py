from tabnanny import verbose
from tkinter import CASCADE
from django.db import models


class Topic(models.Model):

    "Модель, описывающая тему, которую изучает пользователь"

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):

    "Модель, описывающая информацию изученную пользователем по теме"

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Entries"

        def __str__(self) -> str:
            return f"{self.text[:50]}..."
