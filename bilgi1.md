# HTTP - GET ve POST

## Http

<p>1990 yılından beri dünya çapında ağ 
üzerinde kullanılan bir iletişim 
protokolüdür.<br> HTTP‘nin açılımı 
“Hyper Text Transfer Protocol” 
yani “Hiper Metin Transfer Protokolü“dür. <br>
HTTP protokolü ağ üzerinden web sayfalarının 
görüntülenmesini sağlayan protokoldür.<br>
HTTP protokolü istemci-kullanici (PC) 
ile sunucu (server) arasındaki alışveriş kurallarını belirler. <br>
Port olarak ise 80 portunu kullanır. <br>
İstemci sunucuya bir istek gönderir. <br>
Bu istek Internet Explorer, Google Chrome veya 
Mozilla Firefox gibi web browser’lar aracılığıyla iletilir. <br>
Sunucu bu isteği alır ve Apache veya IIS gibi 
web sunucu programları aracılığıyla cevap verir.<br></p>

## HTTP Durum Kodları

<p>İstemci bir sunucu içeriğine HTTP kullanarak ulaşmaya 
çalıştığında sunucu yanıtın durumunu belirten 
bir sayısal kod gönderir. <br>
Bazı durumlarda  HTTP durum kodu (HTTP Status Code) 
istemcinin tarayıcısında da gösterilebilir.<br> 
Örn; 200, 301, 302, 404 ve 500 kodları en yaygın olanlardır.</p><br>

Durum kodlarında 1’den 5’e kadar gruplandırılmıştır.<br>

1xx     Bilgi<br>
2xx     Başarı<br>
3xx     Yönlendirme<br>
4xx     Tarayıcı Hatası<br>
5xx     Sunucu Hatası<br>
<p> <br><br>
HTTP, web browser ile web server arasında
iletişim kurmamızı sağlayan bir protokoldür.<br>
HTTP 1.1 versiyonu (RFC 2616) ile tanımlanan
ve diğer eklentilerle gelen başlıca HTTP metodları şunlardır:</p> <br>
<h4>1-) GET:</h4><br>
<p>Bu metod sunucudan veri almak için kullanılır.<br> 
GET ve POST metodları en sık kullanılan metodlar olup 
sunucudaki kaynaklara erişmek için kullanılırlar.</p><br>

<img src="./get-post.png" width=%80 height=%80>
<br>
<p>GET metodu ile sorgu metinleri URL içinde gönderilebilir. <br>Bunun en önemli faydası kullanıcıların bookmark edebilmeleri ve aynı sorguyu içeren istekleri daha sonra gönderebilmelerini sağlaması ve tarayıcıda önceki sorguların “geri” tuşu ile veya tarayıcı geçmişinden çağrılarak aynı sayfalara ulaşabilmeleridir.<br> Güvenlik açısından URL’lerin ekranda görüntüleniyor olması ve URL’in hedefine ulaşıncaya kadar ve hedef sunucu üzerinde iz kayıtlarında görülebilmesi gönderilen parametrelerin gizlilik ihtiyacı varsa sıkıntı yaratabilir.<br> Bu nedenlerle hassas isteklerin GET ile gönderilmemelidir.</p><br>

<p><h4>2-)POST:<h4> <br><p>Bu metod ile sunucuya veri yazdırabilirsiniz.<br> Bu metodla istek parametreleri hem URL içinde hem de mesaj gövdesinde gönderilebilir.<br> Sadece mesaj gövdesinin kullanımı yukarıda sayılan riskleri engelleyecektir.<br> Tarayıcılar geri butonuna basıldığında POST isteğinin mesaj gövdesinde yer alan parametreleri tekrar göndermek isteyip istemedimizi sorarlar.<br> Bunun temel nedeni bir işlemi yanlışlıkla birden fazla yapmayı engellemektir.<br> Bu özellik ve de güvenlik gerekçeleriyle bir işlem gerçekleştirileceğinde POST metodunun kullanılması önerilir.<br></p>
<p><h4>3-)PUT:<h4> <br> Bu metod ile servis sağlayıcı üzerindeki bir kaynağı güncelleyebilirsiniz.<br> Hangi kaynağı güncelleyecekseniz o kaynağın id’sini göndermek zorunludur.<br></p>
<p><h4>4-)HEAD:<h4> <br> GET metoduyla benzer işleve sahiptir ancak geri dönen yanıtta mesaj gövdesi bulunmaz (yani başlıklar ve içerikleri GET metoduyla aynıdır).<br> Bu nedenle GET mesajı gönderilmeden önce bir kaynağın var olup olmadığını kontrol etmek için kullanılabilir.<br></p>
<p><h4>5-)DELETE:<h4> <br> <p>Bu metod ile sunucudaki herhangi bir veriyi silebilirsiniz.
<p><h4>6-)CONNECT:<h4> <br> <p>Bir proxy sunucu üzerinden başka bir sunucuya bağlanmak ve proxy sunucuyu bir tünel gibi kullanmak için kullanılır.<br></p>
<p><h4>7-)OPTIONS:<h4> <br> <p>Bu metod belli bir kaynak için kullanılabilecek HTTP metodlarını sunucudan sorgulamak için kullanılır.<br></p>
<p><h4>8-)TRACE:<h4> <br> <p>Teşhis amaçlı kullanılan bir metoddur.<br> Sunucu bu metodla gelen istek mesajının içeriğini aynen yanıt gövdesinde geri göndermelidir.<br> Bu yöntemle sunucu ile istemci arasında bir vekil sunucu varsa bu sunucunun ve yaptığı değişikliklerin tespiti mümkün olabilir.<br></p>
<p><h4>9-)PATCH:<h4> <br> <p>Bu metod bir kaynağa istediğiniz küçük çaplı değişimi yapmanızı sağlar.<br></p>
<p><h4>10-)SEARCH:<h4> <br> <p>Bir dizinin altındaki kaynakları sorgulamak için kullanılır.<br></p>