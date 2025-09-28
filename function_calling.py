"""
Basit Function Calling Chatbot
Parent sınıf - diğer chatbot'lar bunu inherit edecek
"""

from datetime import datetime

class FunctionCallingChatbot:
    def __init__(self):
        # Konuşma geçmişini basit bir liste olarak tutuyoruz
        self.conversation_history = [
            {"role": "system", "content": "Sen yardımcı bir asistansın."}
        ]
        self.available_functions = {}
        self.function_calls_made = 0

    def chat(self, user_message: str) -> str:
        """
        Basit taklitçi chat metodu.
        Şimdilik OpenAI API eklemek yerine kullanıcı mesajını yansıtır.
        """
        self.conversation_history.append({"role": "user", "content": user_message})

        # Burada normalde LLM'den yanıt alınır, biz şimdilik dummy cevap döndürüyoruz
        response = f"[Dummy Response] Bana şunu söyledin: {user_message}"
        self.conversation_history.append({"role": "assistant", "content": response})

        return response

    def get_function_definitions(self):
        """Fonksiyon tanımlarını döndürür (child class ekleme yapacak)"""
        return []

    def get_conversation_summary(self):
        """Konuşma özeti döndürür"""
        return {
            "total_messages": len(self.conversation_history),
            "function_calls_made": self.function_calls_made,
            "last_message": self.conversation_history[-1]["content"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
