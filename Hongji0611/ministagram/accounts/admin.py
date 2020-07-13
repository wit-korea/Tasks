from django.contrib import admin
from accounts.models import FollowRelation

class FollowRelationAdmin(admin.ModelAdmin):
    list_display = ('follower', )

admin.site.register(FollowRelation, FollowRelationAdmin)