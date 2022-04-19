#from django.db import models
# Create your models here.
# Veritabani nesnelerinin olusturdugumuz 
# ve sorgulama yaptigimiz katmandir. 
# Ornegin post(gonderi) modeli tanimlanacaksa :
#   . Baslik
#   . Tarih
#   . Icerik
#   . Resim vb.
# bilgilere ihtiyac vardir. Model katmani bu bilgilerin 
# ve daha fazlasinin tanimlandigi yerdir. 
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField



class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=120,verbose_name='Baslik')
    content = RichTextField(verbose_name='Icerik')
    publishing_date = models.DateTimeField(verbose_name='Yayimlanma Tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)


#return f"/post/detail/{self.id}/"
#return "/post/index/"
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})
    
    def get_index(self):
        return reverse('post:index')
    
    def get_update_post(self):
        return reverse('post:update', kwargs={'slug': self.slug})
    
    def get_delete_post(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{counter}'
            counter += 1
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["publishing_date", "id"] #burada Meta clasimizi publishing_date ye bagli kildik. yani en eskiden simdiye,  -publishing_date yazinca tam tersi
        #ordering = ["-id"]
        #ordering = ["publishing_date", "id"] # boyle olunca tarihi ayni olanlarin id alanlarina bakilir