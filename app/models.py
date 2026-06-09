from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=200, verbose_name="Job Title")
    company = models.CharField(max_length=100, verbose_name="Company")
    location = models.CharField(max_length=100, verbose_name="Location")
    experience = models.CharField(max_length=50, verbose_name="Experience Required")
    salary = models.CharField(max_length=50, verbose_name="Salary")
    description = models.TextField(verbose_name="Job Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return f"{self.title} at {self.company}"

class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Title"  # Було "Заголовок"
    )
    author = models.CharField(
        max_length=100, 
        default="Editorial",  # Було "Редакція"
        verbose_name="Author"  # Було "Автор"
    )
    short_description = models.TextField(
        verbose_name="Short Description"  # Було "Короткий опис"
    )
    content = models.TextField(
        verbose_name="Article Content"  # Було "Текст статті"
    )
    image = models.ImageField(
        upload_to="articles/", 
        blank=True, 
        null=True, 
        verbose_name="Image"  # Було "Зображення"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"