from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from decimal import Decimal,ROUND_HALF_UP

# Create your models here.
class service(models.Model):
    objects = None
    service_image = models.FileField(upload_to='food/',max_length=250,null=True,default="/food/set-vector.jpg")
    service_title = models.CharField(max_length=50)
    service_price = models.IntegerField( null=True,default=None)
    service_oldprice = models.IntegerField( null=True, default=0, blank=True)
    service_rating = models.CharField(max_length=20, null=True, default=100,blank=True)
    service_badge = models.CharField(max_length=20, null=True, default="Amazon's Choice", blank=True)
    service_desc = HTMLField(blank=True)
    menu_slug = AutoSlugField(populate_from='service_title', unique=True, null=True, default=None)
    service_deal = models.IntegerField(null=True, default=20, blank=True)
    def save(self,*args,**kwargs):
            if self.service_oldprice and self.service_price:
                discount_val= (1-(self.service_price/self.service_oldprice)) * 100
                self.discount =Decimal(discount_val).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
                super().save(*args,**kwargs)


class mainpage(models.Model):
    mainpage_image = models.FileField(upload_to='mainpage/',max_length=250,null=True,default="/mainpage/set-vector.jpg")
    mainpage_title = models.CharField(max_length=50)
    mainpage_desc = HTMLField()
    mainpage_slug = AutoSlugField(populate_from='mainpage_title', unique=True, null=True, default=None)

class Cart(models.Model):
    items = models.ManyToManyField(service, related_name='carts')  # ← this is the missing line