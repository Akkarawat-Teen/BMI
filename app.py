import streamlit as st

# ตั้งค่าหน้าเว็บหลัก
st.set_page_config(page_title="เว็บสุขภาพและ BMI", page_icon="💪", layout="centered")

st.title("💪 ระบบวิเคราะห์สุขภาพและคำนวณ BMI")
st.markdown("""
ยินดีต้อนรับสู่ **เว็บสุขภาพหลายหน้า (Multi-page App)**  
สร้างด้วย **Streamlit**  
---
คุณสามารถเลือกหน้าได้จากเมนูด้านซ้าย 👈  
เช่น
- คำนวณค่าดัชนีมวลกาย (BMI)
- ดูสถิติสุขภาพทั่วไปของคนไทย
- อ่านข้อมูลเพิ่มเติมเกี่ยวกับโครงการ
---
""")
st.image("https://cdn-icons-png.flaticon.com/512/2966/2966489.png", width=200)
st.success("กรุณาเลือกเมนูด้านซ้ายเพื่อเริ่มต้นใช้งาน 🌿")
