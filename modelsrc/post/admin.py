from django.contrib import admin

# Register your models here.
# Yonetim paneliyle ilgili 
# ayarlarin bulundugu yerdir.
# Bir model olusturulunca modelin 
# yonetim arayuzunu saglamak icin admin 
# dosyasinda tanimlanmasi lazim.
# Uygulama ile ilgili ayarlarin 
# bulundugu yer.
#from .models import Post
from post.models import Post


# ikinci etki
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug']
    #list_display_links = ['title', 'publishing_date'] #  list_editable = ['title'] bu kisim calismasi icin alt satirda title cikarildi
    #list_display_links = ['publishing_date'] eski hale getirdim alt satirda son yorum satiri ders2 nin
    list_display_links = ['title', 'publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    #list_editable = ['title'] # basiligi deirekt guncellememizi sagliyor 
    #prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)