from django.db import models
from django.utils.text import slugify
# Create your models here.

class Furniture(models.Model):
    name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    street = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image1')
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image2')
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image3')
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image4')
    image5 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image5')
    
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if  not self.slug and self.title:
            string = "%s-%s" % (self.id,self.title) 
            self.slug = slugify(string)
        super(Furniture,self).save(*args,**kwargs)

    class Meta:
        db_table="sellpost"
    def __str__(self):
        return self.name + ' - ' + self.title + ' - ' + str(self.price) + 'Rs'

class NewFurnitures(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image1')
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image2')
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image3')
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image4')
    image5 = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Image5')

    slug = models.SlugField(blank=True,null=True)
    
    def save(self,*args,**kwargs):
        if  not self.slug and self.title:
            string = "%s-%s" % (self.id,self.title) 
            self.slug = slugify(string)
        super(NewFurnitures,self).save(*args,**kwargs)

    class Meta:
        db_table="NewFurnitures"
    def __str__(self):
        return self.title + ' - ' + str(self.price) + 'Rs'
