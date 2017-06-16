# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Product(models.Model):
	name=models.CharField(max_length=100,blank=True,null=True)
	description=models.TextField(blank=True,null=True)
	reviews=models.TextField(blank=True, null=True)
	specification=models.TextField(blank=True,null=True)
	price=models.FloatField()
	canpurchase=models.BooleanField(default=True)
	rate=models.IntegerField(default=4)
	author=models.CharField(max_length=126,default="abc@gmail.com")
	
	def __unicode__(self):
		return self.name