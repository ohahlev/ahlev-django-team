from django.contrib import admin
from django.utils.html import format_html
from .models import Member

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'preview_thumbnail', 'date_created', 'last_updated', 'preview_dribbble', 
    'preview_facebook', 'preview_github', 'preview_linkedin', 'preview_twitter']
    search_fields = ['name']
    fieldsets = [
        (None, {
            'fields': ['name', 'position', 'dribbble', 'facebook', 'github', 'linkedin', 'twitter', 
            'photo', 'preview_thumbnail'],
        }),
    ]

    def preview_dribbble(self, obj):
        if obj.dribbble:
            return format_html("<a type='button' href='{}' class='btn-floating btn-sm mx-1 mb-0 btn-dribbble'><i class='fab fa-dribbble'></i></a>", 
            obj.dribbble)
    preview_dribbble.short_description = 'dribbble'
    preview_dribbble.admin_order_field = 'dribbble'

    def preview_facebook(self, obj):
        if obj.facebook:
            return format_html("<a type='button' href='{}' class='btn-floating btn-sm mx-1 mb-0 btn-fb'><i class='fab fa-facebook-f'></i></a>", 
            obj.facebook)
    preview_facebook.short_description = 'facebook'
    preview_facebook.admin_order_field = 'facebook'

    def preview_github(self, obj):
        if obj.github:
            return format_html("<a type='button' href='{}' class='btn-floating btn-sm mx-1 mb-0 btn-git'><i class='fab fa-github'></i></a>", 
            obj.github)
    preview_github.short_description = 'github'
    preview_github.admin_order_field = 'github'

    def preview_linkedin(self, obj):
        if obj.linkedin:
            return format_html("<a type='button' href='{}' class='btn-floating btn-sm mx-1 mb-0 btn-li'><i class='fab fa-linkedin-in'></i></a>", 
            obj.linkedin)
    preview_linkedin.short_description = 'linkedin'
    preview_linkedin.admin_order_field = 'linkedin'

    def preview_twitter(self, obj):
        if obj.twitter:
            return format_html("<a type='button' href='{}' class='btn-floating btn-sm mx-1 mb-0 btn-tw'><i class='fab fa-twitter'></i></a>", 
            obj.twitter)
    preview_twitter.short_description = 'twitter'
    preview_twitter.admin_order_field = 'twitter'

    def preview_thumbnail(self, obj):
        if obj.photo_thumbnail:
            return format_html(u"<img src='{}'/>", obj.photo_thumbnail.url)
    
    preview_thumbnail.short_description = 'Preview'
    readonly_fields = ['preview_thumbnail']
    
    class Media:
        css = {
        'all': (
            'team/css/team_admin.css',
            )
         }


admin.site.register(Member, TeamAdmin)
