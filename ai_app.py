import os
from dotenv import load_dotenv
import google.genai as genai


load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")


if not api_key:
	print("خطا:لم يتم العثور على GEMINI_API_KEY في  ملف .env ")
	exit(1)




client = genai.Client(api_key=api_key)

# اختيار النموذج

MODEL_NAME = "gemini-3.5-flash-lite"

print("جاري الاتصال ب-GEMINI...")
response=model.generate_content("في 3 جمل بسيطه بالعربيه إشرح مفهوم API")



print("\n .......اجابه GEMINI-----")
print(response.text)