CRM Projesi Dokümantasyonu
Customer Relationship Management (Müşteri İlişkileri Yönetimi)

1. Proje Genel Bakış
Günümüzde birçok kuruluş, veri yönetimi ve saklama ihtiyaçlarını karşılamak için Google Drive ve bileşenlerini kullanmaktadır. Bu proje, özellikle IT alanında çalışmak isteyen mülteci kökenli kişiler için mentor görüşmeleri, projelendirme ve mülakat süreçlerini kolaylaştırmak amacıyla tasarlanmıştır. Google Drive üzerinde yapılan bu işlemler, sürekli oturum açma gereksinimi, Excel dosyalarının karışıklığı ve verilere hızlı erişim zorlukları nedeniyle kullanıcı dostu bir uygulama geliştirilmesini hedeflemektedir.

2. Proje Hedefleri
Google Drive ve Google Takvim entegrasyonu ile verilerin otomatik çekilmesi.

Kullanıcı dostu bir arayüz ile başvuru, mentor görüşmesi ve mülakat süreçlerinin kolayca yönetilmesi.

Admin ve kullanıcı rollerine göre farklı erişim seviyeleri sağlanması.

Verilerin filtreleme, arama ve raporlama özellikleri ile etkin bir şekilde yönetilmesi.

3. Sistem Gereksinimleri
3.1. Fonksiyonel Gereksinimler
Kullanıcı Girişi:

Kullanıcı adı ve şifre ile giriş.

Admin ve User rollerine göre farklı menülere yönlendirme.

Başvuru Yönetimi:

Başvuruların listelenmesi, filtrelenmesi ve aranması.

Mükerrer kayıtların tespiti.

Mentor görüşmesi tanımlanmış ve tanımlanmamış başvuruların ayrıştırılması.

Mentor Görüşmesi Yönetimi:

Mentor görüşmelerinin listelenmesi ve aranması.

Çoklu sekme ile farklı görüşme durumlarının yönetilmesi.

Mülakat Yönetimi:

Mülakatların listelenmesi ve aranması.

Proje gönderilmiş ve projesi gelmiş adayların ayrıştırılması.

Admin Yönetimi:

Google Takvim entegrasyonu ile etkinlik kayıtlarının çekilmesi.

Etkinlikte kayıtlı kişilere otomatik mail gönderimi.

3.2. Teknik Gereksinimler
Programlama Dili: Python

Veritabanı: Google Drive (GSpread API)

Web Framework: PyQt6 (GUI için)

API: Google Calendar API, Google Drive API

Diğer Araçlar: Trello (Görev Yönetimi), GitHub (Versiyon Kontrol), UML (Tasarım)

4. Sistem Mimarisi
4.1. Kullanıcı Arayüzü Tasarımı
Giriş Penceresi:

Kullanıcı adı ve şifre giriş alanları.

Giriş butonu ve uyarı mesajları.

Dinamik boyutlandırma ve özelleştirilmiş tasarım (renkler, fontlar, buton stilleri).

Tercihler Menüsü:

Admin ve User rollerine göre farklı menüler.

Başvurular, Mentor Görüşmeleri, Mülakatlar ve Admin Menüsü seçenekleri.

Başvurular Penceresi:

Arama, filtreleme ve listeleme özellikleri.

Mükerrer kayıtların tespiti ve önceki VIT başvurularının kontrolü.

Mentor Görüşmeleri Penceresi:

Görüşmelerin listelenmesi ve aranması.

Çoklu sekme ile farklı durumların yönetimi.

Mülakatlar Penceresi:

Mülakatların listelenmesi ve aranması.

Proje gönderilmiş ve projesi gelmiş adayların ayrıştırılması.

Admin Menüsü:

Google Takvim entegrasyonu ile etkinlik kayıtlarının çekilmesi.

Otomatik mail gönderimi.

4.2. Veri Akış Diyagramı
Kullanıcı girişi sonrası rollerine göre menülere yönlendirme.

Google Drive ve Google Takvim API’ları ile veri çekme ve işleme.

Verilerin filtreleme, arama ve raporlama işlemleri.

5. Proje Yönetimi
5.1. Görev Dağılımı ve Takip
Trello: Görevlerin takibi ve iş bölümü.

Günlük Toplantılar: Her gün 30 dakika süren toplantılar ile ilerleme değerlendirmesi.

5.2. Proje Adımları
Adım: Görev dağılımı, Trello ile proje takibi, UML diyagramları ve arayüz tasarımları.

Adım: Google Drive ve Google Takvim entegrasyonu, Admin Menüsü işlevlerinin tamamlanması.

Adım: Başvurular, Mentor Görüşmeleri ve Mülakatlar pencerelerinin kodlanması.

Adım: Testler, requirements.txt ve README dosyalarının oluşturulması.

Adım: Projenin GitHub’a yüklenmesi ve sunum hazırlığı.

6. Test Planı
Birim Testleri: Her modül için ayrı ayrı testler.

Entegrasyon Testleri: Modüller arası veri akışının kontrolü.

Kullanıcı Kabul Testleri: Son kullanıcılar tarafından sistemin kullanılabilirliğinin test edilmesi.

7. Proje Zaman Çizelgesi
Kick-off Toplantısı: 02/02/2025 (Class_A), 09/02/2025 (Class_B ve Class_G).

Mentor Toplantıları: Her hafta belirli tarihlerde ilerleme değerlendirmesi.

Final Sunumu: 12/02/2025 (Class_A), 19/02/2025 (Class_B ve Class_G).

8. Kaynaklar
Google API Dokümantasyonu: Google Developers

PyQt6 Dokümantasyonu: PyQt6

Trello: Trello

UML Araçları: Lucidchart, Diagrams.net

9. Sonuç
Bu proje, Google Drive ve Google Takvim entegrasyonu ile başvuru, mentor görüşmesi ve mülakat süreçlerini kolaylaştırmayı hedeflemektedir. Kullanıcı dostu arayüzü ve etkin veri yönetimi ile süreçlerin daha verimli hale getirilmesi amaçlanmaktadır.