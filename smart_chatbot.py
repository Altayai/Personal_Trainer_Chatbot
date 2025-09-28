import os
import json
import random
from dotenv import load_dotenv
from openai import OpenAI

# API Key Yükleme
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
class SmartChatbot:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "Sen spor temalı bir asistansın. Kullanıcıya antrenman, beslenme ve motivasyon konularında yardımcı ol."}
        ]

        # ----------------- Fonksiyonlar -----------------
    def antrenman_oner(self, hedef: str, sure: int):
        if hedef == "kardiyo":
            return f"{sure} dk kardiyo: 5 dk ısınma, {sure-10} dk koşu, 5 dk esneme."
        elif hedef == "güç":
            return f"{sure} dk güç antrenmanı: squat, şınav, plank setleri."
        elif hedef == "esneklik":
            return f"{sure} dk yoga ve esneme rutini."
        return "Hedef türünü anlamadım. Kardiyo, güç veya esneklik seçebilirsin."
    
    def kalori_yak(self, aktivite: str, dakika: int, kilo: float):
        oranlar = {"koşu": 10, "yüzme": 8, "bisiklet": 7, "yürüyüş": 4}
        yakilan = oranlar.get(aktivite.lower(), 5) * (kilo / 70) * (dakika / 30) * 100
        return f"{dakika} dk {aktivite} ile yaklaşık {yakilan:.0f} kalori yakarsın."
    
    def protein_ihtiyaci(self, kilo: float):
        ihtiyac = kilo * 1.6
        return f"{kilo} kg için günlük yaklaşık {ihtiyac:.1f} g protein alman önerilir."
    
    def motivasyon_sozu(self):
        sozler = [
            "Vazgeçme, küçük adımlar büyük sonuçlar getirir!",
            "Bugün yaptığın antrenman, yarının gücünü hazırlar.",
            "Disiplin, motivasyonun olmadığı günlerde seni ayakta tutar.",
            "Her ter damlası seni hedeflerine bir adım daha yaklaştırır.",
            "En büyük zafer, kendine meydan okumaktır.",
            "Eğer gökkuşağını görmek istiyorsan, yağmura katlanmalısın.",
            "En çaresiz geceni düşün, Sabah olmadı mı ?",
            "Önemli olan 2 şey var arkadaşlar; Vatan ve Yanındaki Adam, Bu 2 şey için ölür ve öldürürsün!",
            "Başarı, azim ve sabrın birleşimidir."
        ]
        return random.choice(sozler)
    
    def rastgele_challenge(self):
        challengelar = [
            "Bugün 50 şınav yapmayı dene!",
            "En az 3 litre su iç.",
            "20 dakika esneme yap.",
            "Asansör yerine merdiven kullan!",
            "10 km yürüyüşe çık.",
            "Yeni bir sağlıklı tarif dene.",
            "Günün sonunda 5 dakika meditasyon yap.",
            "Bir arkadaşını antrenmana davet et.",
            "Bugün 100 squat yapmayı hedefle.",
        ]
        return random.choice(challengelar)
    
    # ----------------- Function tanımları -----------------
    def get_function_definitions(self):
        return [
            {
                "type": "function",
                "name": "antrenman_oner",
                "description": "Hedefe ve süreye göre antrenman önerisi yapar.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hedef": {"type": "string", "enum": ["kardiyo", "güç", "esneklik"]},
                        "sure": {"type": "integer", "description": "Dakika cinsinden süre"}
                    },
                    "required": ["hedef", "sure"]
                }
            },
            {
                "type": "function",
                "name": "kalori_yak",
                "description": "Aktivite, süre ve kiloya göre tahmini kalori yakımını hesaplar.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aktivite": {"type": "string"},
                        "dakika": {"type": "integer"},
                        "kilo": {"type": "number"}
                    },
                    "required": ["aktivite", "dakika", "kilo"]
                }
            },
            {
                "type": "function",
                "name": "protein_ihtiyaci",
                "description": "Kilo bilgisine göre günlük protein ihtiyacını hesaplar.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kilo": {"type": "number"}
                    },
                    "required": ["kilo"]
                }
            },
            {
                "type": "function",
                "name": "motivasyon_sozu",
                "description": "Rastgele bir motivasyon sözü verir.",
                "parameters": {"type": "object", "properties": {}}
            },
            {
                "type": "function",
                "name": "rastgele_challenge",
                "description": "Rastgele bir spor meydan okuması önerir.",
                "parameters": {"type": "object", "properties": {}}
            }
        ]
    # ----------------- Chat -----------------
    def chat(self, user_input: str):
        self.messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages,
            functions=self.get_function_definitions()
        )

        message = response.choices[0].message
        self.messages.append(message)

        if message.function_call:
                function_name = message.function_call.name
                function_args = json.loads(message.function_call.arguments)

                if hasattr(self, function_name):
                    func = getattr(self, function_name)
                    result = func(**function_args)
                    self.messages.append({"role": "function", "name": function_name, "content": result})
                    return result

        return message.content
    
    # ----------------- Terminalden çalıştırma -----------------
if __name__ == "__main__":
    bot = SmartChatbot()
    print("⛹️​ Spor Chatbot (çıkmak için 'exit' yaz)")
    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Bot: Görüşmek üzere! 🏋️")
            break
        answer = bot.chat(user_input)
        print("Bot:", answer)
