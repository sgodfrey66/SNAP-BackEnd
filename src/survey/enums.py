from django.db import models


class QuestionCategory(models.TextChoices):
    CHOICE = "choice", "choice"
    CURRENCY = "currency", "currency"
    DATE = "date", "date"
    GRID = "grid", "grid"
    NUMBER = "number", "number"
    TEXT = "text", "text"
