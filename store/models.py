from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create Customer Profile
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	
	#DateTimeField is  to display the Entry in date format
	date_modified = models.DateTimeField(User, auto_now=True)
	

	#CharField is to display the Entry in normal text view with a compulsory attribute named max_length
	#The max_length is for denoting the amount of text the Entry can accept 
	#The meaning of the attribute blank=True means if you want to leave the Entry without inserting anything,it's ok
	phone = models.CharField(max_length=20, blank=True)
	address1 = models.CharField(max_length=200, blank=True)


	
	address2 = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200, blank=True)
	state = models.CharField(max_length=200, blank=True)
	zipcode = models.CharField(max_length=200, blank=True)
	country = models.CharField(max_length=200, blank=True)
	old_cart = models.CharField(max_length=200, blank=True, null=True)


	#This method is for displaying the actual name on the admin site
	#Initially the admin site having this model will be a different name which cannot be relatable

	def __str__(self):
		return self.user.username
	

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()

# Automate the profile thing
post_save.connect(create_profile, sender=User)







# Categories of Products
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	#@daverobb2011
	class Meta:
		verbose_name_plural = 'categories'
		#The verbose_name_plural is to change the name of the class to any name you want it to be



# Customers
class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
		
	#EmailField is to display as an email format and returns an error if what is inputed is not an email format
	email = models.EmailField(max_length=100)

	password = models.CharField(max_length=100)


	def __str__(self):
		return f'{self.first_name} {self.last_name}'



# All of our Products
class Product(models.Model):

	name = models.CharField(max_length=100)
	
	#The DecimalField accepts decimal number and has an attributes namely;
	#decimal_places is to tell the Entry how many decimal numbers should it have after the decimal point
	#max_digits denotes how many digits do you want to have in the Entry
	price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

	#A ForeignKey is used to create two table
    #And it takes in an arguemnent .That's the class name
    #we use ForeingKey here cause we are connecting 1 to 1 or 1 to many
    #we add on_delete  cause if we delete a class,what do we want to doafter then
    #Then we use the on_delete=models.CASCADE, to delete all the related object automatically in the website database
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	
	
	description = models.CharField(max_length=250, default='', blank=True, null=True)
	
	image = models.ImageField(upload_to='uploads/product/')



	# Add Sale Stuff
	is_sale = models.BooleanField(default=False)
	sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

	def __str__(self):
		return self.name


# Customer Orders
class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	#IntegerField is for displaying and accepting integer number in th Entry
	quantity = models.IntegerField(default=1)
	address = models.CharField(max_length=100, default='', blank=True)
	phone = models.CharField(max_length=20, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	
	#The BooleanField is for accepting and displayinh only boolean text like True or False in the Entry
	#We set the default to be false using the default attribute
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.product