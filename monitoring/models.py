from django.db import models
class BrandProfile(models.Model):
    brand_name = models.CharField(max_length=120, default='Northstar Pay')
    website = models.URLField(blank=True, default='https://example.com')
    official_handles = models.TextField(blank=True, default='@northstarpay')
    official_publisher = models.CharField(max_length=180, blank=True, default='Northstar Financial Technologies')
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.brand_name
class Detection(models.Model):
    CHANNELS = [('social','Social media'),('app','App store')]
    RISKS = [('High','High'),('Medium','Medium'),('Low','Low')]
    STATUSES = [('Needs review','Needs review'),('Reviewed','Reviewed'),('Official','Official')]
    name = models.CharField(max_length=180)
    handle = models.CharField(max_length=220, blank=True)
    channel = models.CharField(max_length=20, choices=CHANNELS)
    risk = models.CharField(max_length=10, choices=RISKS)
    score = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUSES, default='Needs review')
    signals = models.JSONField(default=list, blank=True)
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
