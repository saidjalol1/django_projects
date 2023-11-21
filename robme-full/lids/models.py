from django.db import models


class Lids(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class LidObjects(models.Model):
    where = (
        ('Center','Markazga'),
        ('center_visits','Markazga kelganlar'),
        ('telegram','Telegram'),
        ('Friend','Friend'),
        ('walked_by','Walked By'),
    )

    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    lid = models.ForeignKey(Lids, on_delete=models.CASCADE, related_name='lid_objects')
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

