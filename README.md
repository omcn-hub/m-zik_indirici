# muzik_indirici
# 🎵 Spotify Top 10 Müzik İndirici & USB Aktarıcı

Bu Python betiği, ismini girdiğiniz bir sanatçının Spotify'daki en popüler 10 şarkısını bulur, YouTube üzerinden MP3 formatında indirir ve belirttiğiniz USB belleğe (veya klasöre) otomatik olarak kopyalar.

Araba yolculukları için USB hazırlamakla uğraşmak istemeyenler için birebir! 🚗💨

## 🚀 Özellikler

* **Spotify Entegrasyonu:** Sanatçının en çok dinlenen "Top 10" listesini çeker.
* **Otomatik İndirme:** `yt-dlp` kullanarak şarkıları yüksek kalitede MP3'e çevirir.
* **USB Transferi:** İndirme bitince dosyaları otomatik olarak hedef klasöre/USB'ye atar.
* **Temizlik:** Geçici klasörleri yönetir.

## 🛠️ Kurulum

Projeyi çalıştırmadan önce aşağıdaki kütüphanelerin yüklü olması gerekir:

1.  **Gerekli Python paketlerini yükleyin:**
    ```bash
    pip install yt-dlp spotipy
    ```

2.  **FFmpeg Kurulumu:**
    MP3 dönüştürme işlemi için bilgisayarınızda [FFmpeg](https://ffmpeg.org/download.html)'in kurulu ve sistem yoluna (PATH) eklenmiş olması gerekir.

## ⚙️ Yapılandırma

Kodun çalışması için kendi Spotify Developer hesabınızdan API anahtarı almanız gerekir.

1.  `muzik_indirici.py` dosyasını açın.
2.  Aşağıdaki alanlara kendi anahtarlarınızı yapıştırın:
    ```python
    SPOTIFY_CLIENT_ID = "SENIN_CLIENT_ID"
    SPOTIFY_CLIENT_SECRET = "SENIN_CLIENT_SECRET"
    ```

## ▶️ Kullanım

Terminal veya komut satırında projeyi çalıştırın:

```bash
python muzik_indirici.py
