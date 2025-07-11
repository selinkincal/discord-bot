# Python 3.10 slim tabanlı bir imaj kullan
FROM python:3.10-slim

# Uygulama klasörünü oluştur
WORKDIR /app

# Gereken dosyaları kopyala
COPY requirements.txt .
COPY bot.py .

# Python bağımlılıklarını yükle
RUN pip install --no-cache-dir -r requirements.txt

# Ortam değişkeni DISCORD_TOKEN ile botu başlat
CMD ["python", "bot.py"]