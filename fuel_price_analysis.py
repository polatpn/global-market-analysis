import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Veri sembolleri: Brent Petrol (BZ=F) ve Dolar/TL (USDTRY=X)
symbols = ['BZ=F', 'USDTRY=X']

print("Petrol ve Kur verileri çekiliyor...")

# 2024 başından itibaren verileri alalım
data = yf.download(symbols, start="2024-01-01")['Close']

# Sütunları isimlendirelim
data.columns = ['Brent_Petrol', 'USD_TRY']

# Basit bir 'Yerel Maliyet Endeksi' oluşturalım (Brent * Dolar)
# Bu, pompadaki fiyat artışının ana itici gücüdür.
data['Maliyet_Endeksi'] = data['Brent_Petrol'] * data['USD_TRY']

# Verileri normalize edelim (Grafikte yan yana görebilmek için)
normalized = (data / data.iloc[0]) * 100

# Görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(normalized['Brent_Petrol'], label='Brent Petrol (Global)', color='blue', alpha=0.7)
plt.plot(normalized['USD_TRY'], label='USD/TRY Kuru (Yerel)', color='green', alpha=0.7)
plt.plot(normalized['Maliyet_Endeksi'], label='Tahmini Akaryakıt Maliyet Baskısı', color='red', linewidth=2)

plt.title('Akaryakıt Fiyatlarını Etkileyen Faktörlerin Analizi (2024-2026)')
plt.ylabel('Başlangıca Göre Değişim (%)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Kaydet
plt.savefig('fuel_analysis.png')
print("Analiz tamamlandı! 'fuel_analysis.png' oluşturuldu.")