import os
import shutil
import yt_dlp
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# ========== SPOTIFY API AYARLARI ==========
SPOTIFY_CLIENT_ID = "df6715ed12d841a2978a582a29000287"
SPOTIFY_CLIENT_SECRET = "a9b37a51fb3d47fe9a4f854e5d842086"

# ========== KULLANICIDAN VERİ AL ==========
sanatci_adi = input("Sanatçının adını yaz: ").strip()
usb_yolu = input("USB sürücü yolunu gir (örn: E:/Muzikler): ").strip()
indirilen_klasor = "gecici_sarkilar"

# ========== SPOTIFY API ==========
auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)

def en_populer_sarkilar(sanatci_adi):
    sonuc = sp.search(q='artist:' + sanatci_adi, type='artist', limit=1)
    if not sonuc['artists']['items']:
        print("Sanatçı bulunamadı.")
        return []
    sanatci_id = sonuc['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(sanatci_id, country='TR')
    return [track['name'] + " " + track['artists'][0]['name'] for track in top_tracks['tracks'][:10]]

# ========== YOUTUBE'DAN MP3 İNDİR ==========
def mp3_indir(sarki_adi, hedef_klasor):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{hedef_klasor}/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f"ytsearch1:{sarki_adi}"])
        except Exception as e:
            print(f"Hata: {e}")

# ========== ANA AKIŞ ==========
if not os.path.exists(indirilen_klasor):
    os.makedirs(indirilen_klasor)

print(f"\n'{sanatci_adi}' sanatçısının en popüler şarkıları indiriliyor...\n")
sarkilar = en_populer_sarkilar(sanatci_adi)

for sarki in sarkilar:
    print(f"İndiriliyor: {sarki}")
    mp3_indir(sarki, indirilen_klasor)

# ========== USB'YE KOPYALA ==========
if not os.path.exists(usb_yolu):
    os.makedirs(usb_yolu)

for dosya in os.listdir(indirilen_klasor):
    if dosya.endswith(".mp3"):
        shutil.copy(os.path.join(indirilen_klasor, dosya), usb_yolu)

print("\nİşlem tamamlandı. Şarkılar USB'ye kopyalandı.")
