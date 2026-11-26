from fastapi import FastAPI

# إنشاء تطبيق FastAPI
app = FastAPI(
    title="First AI API",
    description="أول API لي باستخدام FastAPI",
    version="0.1.0"
)


@app.get("/")
def root():
    """الصفحة الرئيسية - ترجع رسالة ترحيب"""
    return {
        "message": "مرحباً بك في أول API لي!",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/about")
def about():
    """معلومات عن الـ API"""
    return {
        "name": "First AI API",
        "author": "Linamohamed89",
        "purpose": "تعلم بناء APIs مع AI",
        "github": "https://github.com/Linamohamed89/erste_ai"
    }
