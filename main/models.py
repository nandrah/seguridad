from django.db import models

SERVICE_STATUS_CHOICES = (
        (u'PE', u'Pending'),
        (u'RE', u'Resolved'),
    )


class Hacker(models.Model):
    user = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(max_length=100, blank=True, null=True)
    reputation = models.IntegerField(default=0)
    paypal = models.EmailField()

    def __unicode__(self):
        return self.user


class Enterprise(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    enterprise = models.ForeignKey(Enterprise)
    description = models.TextField(blank=True, null=True)
    reputation = models.IntegerField(default=0)
    status = models.CharField((u'status'), max_length=2, choices=SERVICE_STATUS_CHOICES)
    sql_inyection = models.BooleanField()
    RFI = models.BooleanField()
    SCD = models.BooleanField()
    other = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Job(models.Model):
    service = models.ForeignKey(Service)
    hacker = models.ForeignKey(Hacker)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True)


class Comment(models.Model):
    hacker = models.ForeignKey(Hacker)
    job = models.ForeignKey(Job)
    comment = models.CharField(max_length=500, blank=True, null=True)
