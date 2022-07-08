from django.db import models

class User(models.Model):
    name = models.TextField(default="")
    email = models.EmailField(default="")
    number = models.IntegerField(default="")
    User_ID = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return self.name 
    
class Subscription(models.Model):
    plan = models.TextField(default="")
    namesub = models.TextField(default="")
    Service_ID = models.BigAutoField(primary_key=True)
    # usersub = models.OneToOneField(User, on_delete=models.CASCADE)
    # usersubs = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.namesub

class Feedback(models.Model):
    nameuser = models.TextField(default="")
    game = models.TextField(default="")
    response = models.TextField(default="")
    Feedback_ID= models.BigAutoField(primary_key=True)
    # User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nameuser

class Guides(models.Model):
	Guide_ID = models.BigAutoField(primary_key=True)

	def __str__(self):
		return self.Guide_ID
    
class Feeds(models.Model):
    News_ID = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return self.News_ID 
    
