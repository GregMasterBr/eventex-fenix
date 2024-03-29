from django.contrib import admin
from django.utils.html import format_html
from eventex.core.models import Speaker, Contact, Talk, Course

class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1
    #max_num = 1

# Register your models here.
class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['photo_img', 'name', 'website_link', 'email', 'phone']
    search_fields = ('name',)

    def website_link(self, obj):
        return format_html('<a href="{0}" target="blank">{0}</a>', obj.website)
    
    website_link.short_description = 'website'

    def photo_img(self,obj):
        return format_html('<img width="32px" src="{0}" alt="foto do palestrante" />', obj.photo)
    
    photo_img.allow_tags = True
    photo_img.short_description = 'foto'    


    def email(self, obj):
        return obj.contact_set.emails().first()    
   
    email.short_description = 'e-mail'

    def phone(self, obj):
        return obj.contact_set.phones().first()    


    phone.short_description = 'telefone'

class TalkModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(course=None)

admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course)