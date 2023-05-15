from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title
