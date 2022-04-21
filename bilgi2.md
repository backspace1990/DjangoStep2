# GET vs POST
<img src="./getvspost.jpeg" width=%80 height=%80>

<p>GET methodu kullanıldığında istekler URL kısmında gönderilir.<br> Gönderilen bilgiler URL’de görüntülendiği için güvenlik riski yüksektir ancak POST metoduna göre daha hızlıdır.</p>
<br>
Ornegin: /test/demo_form.php?name1=value1&name2=value2 <br>
<p>POST metodu ise URL’de görüntülenmesi istemediğimiz istekler için kullanılır.<br> Gönderilen bilgiler URL’de görünmediği için daha güvenlidir ancak GET methoduna göre daha yavaştır.<br> Yani POST metodunda form alanları HTTP REQUEST HEADER içinde kodlanmış olarak gider, URL’de gözükmez. <br>POST işleminde her türlü dosyayı post edebiliriz: XML,Image, File post edebiliriz.</p><br>
Orengin: <br>
POST /test/demo_form.php HTTP/1.1<br>
Host: w3schools.com<br>
name1=value1&name2=value2<br>

<p>
GET ile veri göndermede karakter limiti varken POST’ta böyle bir limit yoktur. <br>Karakter limiti GET metodunda 2048 karakterdir.<br>
GET’i ön plana çıkaran bir farktan bahsedelim.<br> GET ile değişkenler URL’de yer aldığı için sayfayı değişken değerleri kaybolmadan yer imlerine atmak mümkündür. <br>Yani GET ile bir sayfa içeriğini sunucudan almak için tekrar tekrar forma veri girmeye ya da sayfa içi tıklamalar yapılmasına gerek yoktur.<br> Dolayısıyla hazır URL’yi yer imlerine atarak kullanıcı zahmetten kurtarılmış olur.<br> POST’ta ise kullanıcı daha önce geldiği aşamaya(sayfa içeriğine) tekrar varabilmek için forma veri girme ya da tıklama zahmetlerine katlanmak zorundadır.<br>
GET’in POST’a karşı bir diğer dezavantajı şudur: multi-part binary türündeki verilerin gönderimi. <br>“multi-part binary” ile kastedilen şey dosyadır.<br> Örneğin; resimdir. POST ile forma bir resim koyup sunucuya upload edebiliriz.<br> Fakat GET ile bu mümkün değildir.
</p>
