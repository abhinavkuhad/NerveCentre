from django.db import models

# Create your models here.

class NewsCentre(models.Model):
    class Meta:
        db_table = 'news_centre'
        unique_together = ('title','news_url')

    id = models.UUIDField(max_length=32, primary_key=True)
    source_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50,null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    news_url = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    content = models.TextField(null=True)

class Journalist(models.Model):
    class Meta:
        db_table = 'journalists'
    id = models.UUIDField(max_length=32, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class ResourceCentre(models.Model):
    class Meta:
        db_table = 'resource_centre'
        unique_together = ('newscentre', 'journalist')

    id = models.UUIDField(max_length=32, primary_key=True)
    journalist = models.ForeignKey(Journalist, related_name='resourcecentres', on_delete=models.CASCADE)
    journalist_fname = models.CharField(max_length=20)
    journalist_lname = models.CharField(max_length=20)
    current_status = models.CharField(max_length=15)
    assigned_date = models.DateTimeField()
    newscentre = models.ForeignKey(NewsCentre, related_name='resourcecentres', on_delete=models.CASCADE)


