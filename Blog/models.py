from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from spacy import blank
from sqlalchemy import null

class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    STATUS = (
        ('0','Draft'),
        ('1','Publish'),
    )
    SECTION = (
        ('Trending','Trending'),
        ('Popular','Popular'),
    )
    fetured_image = models.ImageField(upload_to = 'Images/', null=True,blank = True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Topic, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    content = RichTextField()
    slug = models.SlugField(max_length=500,null=True,unique=True,blank = True)
    status  = models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=200)

    def __str__(self) -> str:
        return self.title

def create_slug(instance,new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug


def pre_save_post_reciver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciver,Post)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name