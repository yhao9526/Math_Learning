import streamlit as st
import pandas as pd
from utils.checker import check_answer
import os

# 载入题库
questions = pd.read_csv('data/questions.csv')

# 初始状态
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("📖 微积分题库练习")

# 获取当前题目
q_index = st.session_state.current_question
if q_index < len(questions):
    question = questions.iloc[q_index]
    st.write(f"### 📌 第 {q_index+1} 题： {question['question']}")

    user_answer = st.text_input("✏️ 你的答案：")

    if st.button("提交答案"):
        if check_answer(user_answer, question['answer']):
            st.success("✅ 正确！")
            st.session_state.score += 1
        else:
            st.error(f"❌ 错误！正确答案是：{question['answer']}")

        # 答题记录
        log = f"{question['id']},{question['question']},{user_answer},{question['answer']}\n"
        with open('results/user_logs.csv', 'a', encoding='utf-8') as f:
            f.write(log)

        st.session_state.current_question += 1
        st.experimental_rerun()

else:
    st.balloons()
    st.write("🎉 全部题目完成！")
    st.write(f"你的正确率是：{st.session_state.score / len(questions) * 100:.2f}%")

# 进度
st.progress(st.session_state.current_question / len(questions))
