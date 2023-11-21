from django.db import models
class Staff(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    

    def get_full_name(self):
        return str(self.name) + " " + str(self.surname)

    def __str__(self):
        return self.name
    

class TextMessage(models.Model):
    date_send = models.DateTimeField(auto_now_add=True)
    added_text_message = models.DateTimeField(auto_now=True)
    from_who = models.CharField(max_length=200)
    to_who = models.CharField(max_length=200)
    body = models.TextField()
    # student = models.ForeignKey(Students,on_delete=models.DO_NOTHING, related_name='text_message', blank=True, null=True)
    # Teacher = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING, related_name='text_message', blank=True, null=True)

    def __str__(self):
        return str(f" send to {self.to_who }")