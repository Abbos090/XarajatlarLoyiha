from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)  # foydalanuvchi ismi
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # sarflagan pul
    date = models.DateField(auto_now=True)  # avtomatik sana

    def __str__(self):
        return f"{self.name} - {self.amount} so'm - {self.date}"