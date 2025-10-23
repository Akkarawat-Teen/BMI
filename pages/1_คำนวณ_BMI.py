
import streamlit as st

st.title("⚖️ คำนวณดัชนีมวลกาย (BMI)")

st.write("กรอกข้อมูลของคุณเพื่อคำนวณ BMI:")

# รับข้อมูลจากผู้ใช้
height = st.number_input("ส่วนสูง (เซนติเมตร)", min_value=100.0, max_value=250.0, step=0.1)
weight = st.number_input("น้ำหนัก (กิโลกรัม)", min_value=20.0, max_value=200.0, step=0.1)

if st.button("คำนวณ BMI"):
    bmi = weight / ((height/100) ** 2)
    st.success(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

    # วิเคราะห์ผล
    if bmi < 18.5:
        st.warning("น้ำหนักน้อยกว่ามาตรฐาน")
    elif 18.5 <= bmi < 23:
        st.success("น้ำหนักอยู่ในเกณฑ์ปกติ ✅")
    elif 23 <= bmi < 25:
        st.warning("น้ำหนักเกินเล็กน้อย")
    elif 25 <= bmi < 30:
        st.error("อ้วนระดับ 1 ⚠️")
    else:
        st.error("อ้วนระดับ 2 🚨")

st.info("💡 สูตรคำนวณ BMI = น้ำหนัก (กก.) ÷ (ส่วนสูงเป็นเมตร)^2")
