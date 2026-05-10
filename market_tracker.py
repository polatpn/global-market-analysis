import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Küresel varlıklar: Altın (GC=F), Petrol (CL=F), S&P 500 (^GSPC)
assets = ['GC=F', 'CL=F', '^GSPC']

print("Küresel veriler Yahoo Finance üzerinden çekiliyor...")

# 2024'ten bugüne günlük kapanış verilerini çekelim
data = yf.download(assets, start="2024-01-01")['Close']

# Sütun isimlerini düzenleyelim (Veri çekilirken gelen sıraya göre)
# Not: Yfinance alfabetik çeker: CL=F (Petrol), GC=F (Altın), ^GSPC (S&P 500)
data.columns = ['Ham Petrol', 'Altın', 'S&P 500']

# Verileri normalize edelim (Hepsini 100'den başlatalım ki kıyaslansın)
normalized_data = (data / data.iloc[0]) * 100

# Grafik oluşturma
plt.figure(figsize=(12, 6))
plt.plot(normalized_data)
plt.title('Küresel Ekonomik Göstergeler (2024 - 2026)')
plt.xlabel('Tarih')
plt.ylabel('Başlangıca Göre Değişim (%)')
plt.legend(['Ham Petrol', 'Altın', 'S&P 500'])
plt.grid(True)

# Grafiği dosya olarak kaydet
plt.savefig('ekonomik_analiz.png')
print("Başarılı! Analiz grafiği 'ekonomik_analiz.png' adıyla kaydedildi.")