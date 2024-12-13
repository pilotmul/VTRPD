from django.db import models

# Create your models here.
class Click(models.Model):
    ip_address = models.GenericIPAddressField()
    session_key = models.CharField(max_length=100, unique=True, null=True, blank=True)
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Antal klik"
        verbose_name_plural = "antal klik"

    def __str__(self):
        return f"Click from {self.ip_address} at {self.timestamp}"


from django.db import models

class CodeSubmission(models.Model):
    code = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.code} submitted at {self.timestamp}"

class AttemptCounter(models.Model):
    attempts = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Angivet kode"
        verbose_name_plural = "Angivet kode"

    def __str__(self):
        return f"Total attempts: {self.attempts}"