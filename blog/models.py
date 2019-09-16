from django.db import models
#create a blog models
class blog(models.Model):
    title=models.CharField(max_length=255)
    pub_data=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to='images/')
    def summary(self):
        return self.body[0:100]
    def pub_date_pretty(self):
        return self.pub_data.strftime('%b %e %Y')
    def __str__(self):
        return self.title

#pub datetime
#body
#image
#add the blog app to the settings
#create a migrations
#migrate
#add to the adminlogentry
