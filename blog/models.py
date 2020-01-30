from django.db import models
from django.shortcuts import  reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    """
    Function for generating unique slug.
    """
    new_slug = slugify(s,allow_unicode = True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    """
    Post model.Stores a single blog related to model Tag 
    with many to many relationship.
    """
    title = models.CharField(max_length = 150,db_index = True)
    slug = models.SlugField(max_length = 150,blank = True ,unique = True)
    body = models.TextField(blank=True,db_index= True)
    tags = models.ManyToManyField('Tag',blank = True,related_name='posts')
    date_pub = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """
        Method for calculating the canonical URL for viewing object.        
        """
        return reverse('post_detail_url',kwargs={'slug':self.slug})

    def get_update_url(self):
        """
        Method for calculating the canonical URL for editing object.        
        """
        return reverse('post_update_url',kwargs = {'slug':self.slug})

    def get_delete_url(self):
        """
        Method for calculating the canonical URL for deleting object.        
        """
        return reverse('post_delete_url',kwargs = {'slug':self.slug})


    def save(self,*args,**kwargs):
        """
        Overriding method save for blank slug.
        """
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-date_pub']

        
class Tag(models.Model):
    """
    Tag model.Stores a single tag related to model Post 
    with many to many relationship.
    """
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50,unique = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Method for calculating the canonical URL for viewing object.        
        """
        return reverse('tag_detail_url',kwargs={'slug':self.slug})

    def get_update_url(self):
        """
        Method for calculating the canonical URL for editing object.        
        """
        return reverse('tag_update_url',kwargs = {'slug':self.slug})

    def get_delete_url(self):
        """
        Method for calculating the canonical URL for deleting object.        
        """
        return reverse('tag_delete_url',kwargs = {'slug':self.slug})

    class Meta:
        ordering = ['title']
