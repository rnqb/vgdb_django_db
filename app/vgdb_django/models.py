from django.db import models


class sales(models.Model):
    game_title = (models.CharField(max_length=999))
    copies_sold = (models.CharField(max_length=999))
    release_year = (models.CharField(max_length=999))


class publishers(models.Model):
    publisher_name = (models.CharField(max_length=999))
    publisher_address = (models.CharField(max_length=999, null=True))


class games(models.Model):
    # id = automatically created with Django ORM. This will be Primary Key and set to UNIQUE/NON NULL
    # NOT NULL IS DEFAULT, BLANK IS FALSE BY DEFAULT
    game_title = models.CharField(max_length=999, null=False, blank=False)
    game_platform = models.CharField(max_length=999)
