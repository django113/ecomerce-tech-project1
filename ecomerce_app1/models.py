from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

"""
    product 
	name
	discription
	user
	colors
	grade
	rating
	size
	qulaity
	image
"""


class Products(models.Model):
    Grade = [
        ('A1', 'A1'),
        ('B1', 'B1'),
        ('C1', 'C1'),
    ]
    Ratings = [
        (1,'good'),
        (2,'very good'),
        (3,'bad'),
        (4,'very bad'),
    ]
    # Sizes = [
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),

    # ]
    Quality = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Big', 'Big'),
        ('Other', 'Other'),

    ]

    # Status= [
    #     ('InStock','InStock'),
    #     ('OutStock','OutStock'),
    # ]
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='Products', default='')
    description = models.TextField()
    colors = models.CharField(max_length=50,help_text="Color Code Enter only")
    grade = models.CharField(max_length=50, choices=Grade)
    rating = models.CharField(max_length=50, choices=Ratings)
    quality = models.CharField(max_length=50, choices=Quality)
    # size = models.PositiveBigIntegerField()
    size = models.CharField(max_length=50,null=True,blank=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)  # automatic add
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)

    # product details

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    


