import google.generativeai as genai

# !!! ضع مفتاح الـ API الخاص بك هنا !!!
API_KEY = '*******' 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(prompt):
    print(f"إرسال الطلب إلى Gemini: {prompt}")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"حدث خطأ أثناء الاتصال بـ Gemini: {e}")
        return "عذراً، أواجه مشكلة في الاتصال بالخادم."

# --- اختبار المرحلة 2 ---
if __name__ == "__main__":
    test_prompt = "اشرح لي نظرية النسبية ببساطة"
    reply = get_gemini_response(test_prompt)
    print(f"رد Gemini: {reply}")