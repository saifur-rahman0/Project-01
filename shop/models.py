from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('K', 'Kids'),
        ('M', 'Mens'),
        ('W', 'Womens'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class LatestNews(models.Model):
    title = models.CharField(max_length=255, help_text='The title of the news', default='')
    description = models.TextField(help_text='The full description of the news', null=True, blank=True)
    is_active = models.BooleanField(default=True, help_text='Whether this news item is active and should be shown')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'