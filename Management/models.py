from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    cat=models.ForeignKey(Category, on_delete = models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name+'<-->' + str(self.cat.name)

class Product(models.Model):
    subCat=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=50,null=True,blank=True)
    discription=models.TextField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    discountpercent=models.FloatField(null=True,blank=True)
    img1=models.FileField(null=True,blank=True)
    img2=models.FileField(null=True,blank=True)
    img3=models.FileField(null=True,blank=True)
    ratings=models.FloatField(null=True,blank=True)
    returnPolicy=models.BooleanField(null=True,blank=True,default=True)
    available=models.BooleanField(null=True,blank=True,default=True)
    cod=models.BooleanField(null=True,blank=True)
    
    def __str__(self):
        return self.title +'<-->' + str(self.subCat.name)
    
 
 
class ContactForm(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True) 
    email=models.EmailField(null=True,blank=True)
    msg=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name +'<-->' +str(self.name)
    
      
    
       
    
