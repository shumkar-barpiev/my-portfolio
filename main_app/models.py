from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Home_dev_information(models.Model):

    full_name = models.CharField(null=True, max_length=30)
    dev_email_account = models.CharField(null=True, max_length=60)
    kind_of_developer = models.CharField(null=True, max_length=40)
    developer_img = models.ImageField(blank=True, null=True, upload_to='owner/')

    def __str__(self):
        return self.full_name



class About_dev_information(models.Model):
    about_description = models.TextField(null=True)
    my_cv_file = models.FileField(upload_to='media',default='settings.MEDIA_ROOT/media/anonymous.jpg')

    def __str__(self):
        return self.about_description

class What_I_do_dev_information(models.Model):
    kind_dev_title = models.CharField(max_length=30)
    kind_dev_description = models.TextField(null=True)

    def __str__(self):
        return self.kind_dev_title

class Experience_and_starting_dev_information(models.Model):
    starting_and_nowadays_years_dev_title = models.CharField(null=True, max_length=30)
    experience_year = models.IntegerField(default=0)
    projects_number = models.IntegerField(default=0)


    def __str__(self):
        return self.starting_and_nowadays_years_dev_title

class My_Recent_Works_dev_information(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    project_title = models.CharField(max_length=30)
    project_img = models.ImageField(blank=True, null=True, upload_to='images/')
    slug = models.SlugField(max_length=250,null=True, unique_for_date='publish')
    project_link = models.CharField(null=True, max_length=50)
    project_description = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='all_projects')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def get_absolute_url(self):
        return reverse('home:post_single', args=[self.slug])

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.project_title

class My_Skills_dev_information(models.Model):
    skills_title = models.CharField(null=True, max_length=30)
    skills_number = models.IntegerField(default=0)

    def __str__(self):
        return self.skills_title

class My_Languages_dev_information(models.Model):
    language_title = models.CharField(null=True, max_length=30)
    language_degree = models.IntegerField(default=0)

    def __str__(self):
        return self.language_title

class Social_links_dev_information(models.Model):
    facebook_link = models.CharField(null=True, max_length=60)
    instagram_link = models.CharField(null=True, max_length=60)
    github_link = models.CharField(null=True, max_length=60)
    youtube_link = models.CharField(null=True, max_length=60)
    telegram_link = models.CharField(null=True, max_length=60)

    def __str__(self):
        return self.facebook_link
