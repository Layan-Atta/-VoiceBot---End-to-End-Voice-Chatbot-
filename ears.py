import speech_recognition as sr

def listen_to_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("تفضل، أنا أسمعك...")
        # ضبط الحساسية للضوضاء المحيطة
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

    try:
        # استخدام محرك جوجل للتعرف على الصوت (لا يتطلب مفتاح API)
        text = r.recognize_google(audio, language='ar-AR')
        print(f"أنت قلت: {text}")
        return text
    except sr.UnknownValueError:
        print("عذراً، لم أفهم ما قلت.")
        return None
    except sr.RequestError as e:
        print(f"خطأ في الاتصال بخدمة جوجل؛ {e}")
        return None

# --- اختبار المرحلة 1 ---
if __name__ == "__main__":
    listen_to_mic()