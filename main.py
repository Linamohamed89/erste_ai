from fastapi import FastAPI
from pydantic import BaseModel, Field

# إنشاء تطبيق FastAPI
app = FastAPI()


# تعريف شكل البيانات المتوقعة من العميل
class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)


@app.get("/")
def root():
    """الصفحة الرئيسية"""
    return {
        "message": "مرحباً بك في أول API لي!",
        "status": "running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    """يستقبل سؤالاً ويرجع رسالة تأكيد (سنربطه بـ Gemini في المهمة القادمة)"""
    return {
        "status": "received",
        "question_received": request.question,
        "length": len(request.question),
        "message": "تم استلام السؤال بنجاح. (Gemini integration قادم)"
    }
