from django.contrib import admin
from .models import BrandProfile, Detection
@admin.register(BrandProfile)
class BrandProfileAdmin(admin.ModelAdmin): list_display=('brand_name','website','updated_at')
@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin): list_display=('name','channel','risk','score','status','created_at'); list_filter=('channel','risk','status'); search_fields=('name','handle','reason')
