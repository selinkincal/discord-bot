# discord-bot
 Python Discord Bot

Basit bir Discord botu. Kullanıcı ne yazarsa aynısını cevap olarak döner. 
Python ile yazılmıştır ve `discord.py` kütüphanesini kullanır.

## 🔧 Kurulum

1. **Python 3.10+** yüklü olduğundan emin ol.  
   İndir: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Sanal ortam oluştur ve aktif et:**

```bash
python -m venv venv       # Sanal ortam oluştur
venv\Scripts\activate    # Sanal ortamı aktif et (Windows için)
pip install discord.py   # discord.py kütüphanesini yükle
# Eğer uv yüklüyse:
uv pip install discord.py

## 🚀 Botu Çalıştırmak

`bot.py` dosyasında aşağıdaki satıra kendi bot tokenini yaz:

```python
client.run("BURAYA_BOT_TOKENİNİ_YAZ")

python bot.py    # Sonrasında terminalden çalıştır

