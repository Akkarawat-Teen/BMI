import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 ข้อมูลสถิติสุขภาพของคนไทย")

data = {
    "ช่วงอายุ": ["18-25", "26-35", "36-45", "46-60", "60+"],
    "ค่าเฉลี่ย BMI": [21.5, 23.1, 24.8, 25.3, 24.5]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.write("กราฟแสดงค่าเฉลี่ย BMI ตามช่วงอายุ:")

fig, ax = plt.subplots()
ax.bar(df["ช่วงอายุ"], df["ค่าเฉลี่ย BMI"])
ax.set_xlabel("ช่วงอายุ")
ax.set_ylabel("ค่า BMI เฉลี่ย")
ax.set_title("ค่าเฉลี่ย BMI ของคนไทยตามช่วงอายุ")
st.pyplot(fig)

st.caption("ข้อมูลสมมติ เพื่อใช้เป็นตัวอย่างในการสอน Streamlit")
