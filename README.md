# Personal_Trainer_Chatbot

**Personal_Trainer_Chatbot**, spor ve fitness odaklı bir yapay zeka asistanıdır. Kullanıcıların antrenman, beslenme ve motivasyon ihtiyaçlarına yardımcı olur. Python ve OpenAI API kullanılarak geliştirilmiştir ve terminal üzerinden interaktif şekilde çalışır.

---

## 📂 Proje Dizini

```
LLM_Chatbot/
│
├─ __pycache__/            # Python önbellek dosyaları
├─ venv/                   # Sanal ortam
├─ .env                    
├─ .gitignore
├─ function_calling.py     # Parent class veya fonksiyonlar (opsiyonel)
├─ LICENSE
└─ smart_chatbot.py        # Ana chatbot dosyası
```

---

## ⚙️ Kurulum

1. Repo’yu klonlayın veya dosyaları indirin.
2. Sanal ortam oluşturun ve aktif edin:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Gerekli paketleri yükleyin:
   ```bash
   pip install openai python-dotenv
   ```
4. Chatbot’u çalıştırın:
   ```bash
   python smart_chatbot.py
   ```

---

## 🤖 Kullanım

Terminalde chatbot ile interaktif olarak sohbet edebilirsiniz.  
Çıkmak için `exit` veya 'q' yazmanız yeterlidir.

---

## 🔹 Fonksiyonlar

Personal_Trainer_Chatbot, 5 ana fonksiyon içerir:

1. **antrenman_oner(hedef, sure)**
   - Hedef ve süreye göre antrenman önerir.
   - Hedefler: `kardiyo`, `güç`, `esneklik`
   - Örnek kullanım:
     ```python
     bot.chat("Bugün için 20 dk kardiyo antrenmanı önerir misin?")
     ```
     **Cevap Örneği:**
     ```
     20 dk kardiyo: 5 dk ısınma, 10 dk koşu, 5 dk esneme.
     ```

2. **kalori_yak(aktivite, dakika, kilo)**
   - Aktivite, süre ve kilo bilgisine göre tahmini kalori yakımını hesaplar.
   - Örnek kullanım:
     ```python
     bot.chat("70 kiloyum, 30 dk koşuda kaç kalori yakarım?")
     ```
     **Cevap Örneği:**
     ```
     30 dk koşu ile yaklaşık 300 kalori yakarsın.
     ```

3. **protein_ihtiyaci(kilo)**
   - Kullanıcının kilosuna göre günlük protein ihtiyacını hesaplar.
   - Örnek kullanım:
     ```python
     bot.chat("80 kiloyum, günlük protein ihtiyacım ne kadar?")
     ```
     **Cevap Örneği:**
     ```
     80 kg için günlük yaklaşık 128 g protein alman önerilir.
     ```

4. **motivasyon_sozu()**
   - Kullanıcıya rastgele motivasyon sözü verir.
   - Örnek kullanım:
     ```python
     bot.chat("Beni motive et")
     ```
     **Cevap Örneği:**
     ```
     Disiplin, motivasyonun olmadığı günlerde seni ayakta tutar.
     ```

5. **rastgele_challenge()**
   - Kullanıcıya rastgele bir spor meydan okuması önerir.
   - Örnek kullanım:
     ```python
     bot.chat("Bugün için bana bir challenge ver")
     ```
     **Cevap Örneği:**
     ```
     20 dakika esneme yap.
     ```

---

## 💬 Örnek Soru-Cümleleri

- "70 kiloyum, günlük protein ihtiyacım ne kadar?"  
- "30 dakika koşuda kaç kalori yakarım?"  
- "Bugün için antrenman önerisi verir misin? Kardiyo, 20 dk."  
- "Beni motive et"  
- "Bugün için bana bir challenge ver"  

---

## 🔹 Teknolojiler

- Python 3.x  
- OpenAI API (`gpt-4o-mini`)  
- dotenv  
- PowerShell veya terminal üzerinden interaktif kullanım  

---

## 📌 Notlar

- Proje MIT Lisansı ile lisanslanmıştır.
- `venv/` ve önbellek dosyaları `.gitignore` ile dışlanmıştır.  
- Proje tamamen terminal tabanlıdır, ancak ileride Streamlit veya web arayüzü ile genişletilebilir.
```

