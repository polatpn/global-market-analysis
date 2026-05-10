import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Daha kararlı çalışan tickerlar: CL=F (Petrol) ve USDTRY=X (Dolar)
symbols = ['CL=F', 'USDTRY=X']

print("Veriler çekiliyor ve temizleniyor...")

# Verileri çekelim
raw_data = yf.download(symbols, start="2024-01-01")['Close']

# EKSİK VERİ KONTROLÜ: Boş satırları bir önceki günle doldur veya sil
data = raw_data.ffill().dropna() 

# Sütun isimlerini garantiye alalım
# yfinance alfabetik getirir: CL=F (Petrol), USDTRY=X (Dolar)
data.columns = ['Petrol', 'Dolar']

# Yerel Maliyet Endeksi
data['Maliyet_Endeksi'] = data['Petrol'] * data['Dolar']

# Normalizasyon: İlk GEÇERLİ güne bölüyoruz
normalized = (data / data.iloc[0]) * 100

# Görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(normalized['Petrol'], label='Petrol (Global)', color='blue', alpha=0.6)
plt.plot(normalized['Dolar'], label='Dolar/TL (Yerel)', color='green', alpha=0.6)
plt.plot(normalized['Maliyet_Endeksi'], label='Toplam Maliyet Baskısı', color='red', linewidth=2.5)

plt.title('Akaryakıt Maliyet Analizi: Dolar mı Petrol mü?')
plt.ylabel('Değişim (%) (Başlangıç = 100)')
plt.legend()
plt.grid(True, alpha=0.3)

# Kaydet
plt.savefig('fuel_analysis.png')
print("İşlem tamam! Şimdi 'fuel_analysis.png' dosyasını tekrar kontrol et.")