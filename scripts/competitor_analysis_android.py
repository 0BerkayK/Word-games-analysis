from google_play_scraper import app, search
import pandas as pd

# İncelenecek oyun isimleri
games = ["Wordscapes", "Word Cookies", "Word Connect", "Word Life", "Word Calm"]

# Bilgileri toplayacağımız liste
app_data = []

for game in games:
    # İlk çıkan uygulamayı al
    result = search(game, n_hits=1)[0]
    package_name = result['appId']

    # Detayları getir
    details = app(package_name)

    app_data.append({
        "Oyun Adı": details['title'],
        "Geliştirici": details['developer'],
        "Puan": details['score'],
        "Yorum Sayısı": details['reviews'],
        "İndirme": details.get('installs', 'N/A'),
        "Kategori": details['genre'],
        "Açıklama (ilk 200 karakter)": details['description'][:200],
        "Güncelleme Tarihi": details['updated'],
        "Paket Adı": package_name,
        "URL": f"https://play.google.com/store/apps/details?id={package_name}"
    })

# DataFrame'e çevir ve kaydet
df = pd.DataFrame(app_data)
df.to_csv("../data/competitor_analysis.csv", index=False)

print("CSV oluşturuldu: competitor_analysis.csv")
