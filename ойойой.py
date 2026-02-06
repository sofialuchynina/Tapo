import streamlit as st
import random

# Налаштування сторінки
st.set_page_config(page_title="SLV")

# Оновлений CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FFE4E1;
    }
    h1 {
        color: #D02090 !important;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
    }
    .stTextInput label {
        color: #000000 !important;
        font-weight: bold;
    }
    input {
        color: #000000 !important; /* Виправлено на чорний */
    }
    ::placeholder {
        color: #4B4B4B !important;
    }
    div.stButton > button {
        background-color: #FFC0CB !important;
        color: #5D2E46 !important;
        border: 2px solid #FFB6C1 !important;
        border-radius: 20px !important;
        width: 100% !important;
        font-weight: bold !important;
    }
    /* Колір кнопки, коли вона неактивна */
    div.stButton > button:disabled {
        background-color: #E0E0E0 !important;
        color: #A0A0A0 !important;
        border-color: #D3D3D3 !important;
    }
    .prediction-box {
        background-color: #FFF0F5;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #FFB6C1;
        text-align: center;
        font-size: 20px;
        color: #5D2E46;
        margin-top: 30px; 
        margin-bottom: 60px; 
        box-shadow: 0px 4px 15px rgba(208, 32, 144, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Забий на розвиток, деградуй з Нами!!!")

# Поле введення
question = st.text_input("Давай ніщєта, задавай питання:", placeholder="тут")

# ЛОГІКА: Перевіряємо, чи введено питання
# strip() прибирає пробіли, щоб не можна було просто «натикати» пробілів
is_disabled = not question.strip()

# Контейнер для результату
result_container = st.container()

def show_prediction(category, options):
    res = random.choice(options)
    result_container.empty() 
    with result_container:
        st.markdown(f'<div class="prediction-box"><b>{category}:</b><br>{res}</div>', unsafe_allow_html=True)

# Кнопки в два стовпчики
col1, col2 = st.columns(2)

with col1:
    if st.button("Кохання/Дружба", disabled=is_disabled):
        show_prediction("Про любов", ["кохання", "френдзона", "пішов він нахуй"])
    if st.button("Коли це буде?", disabled=is_disabled):
        show_prediction("Час", ["дууууууже скоро (1-2 дні)", "дуже скоро (1-2 тижні)", "скоро (1-2 місяці)", "ще не визначено", "ну піздєц"])
    if st.button("Порада дня", disabled=is_disabled):
        show_prediction("Порада", ["будь уважним до деталей", "довіряй інтуїції", "зроби паузу і відпочинь"])
    if st.button("Пачіму?", disabled=is_disabled):
        show_prediction("Пачіму", ["бо даун", "бо красавчік"])

with col2:
    if st.button("Так чи Ні?", disabled=is_disabled):
        show_prediction("Відповідь", ["так", "ні"])
    if st.button("Пророцтво", disabled=is_disabled):
        show_prediction("Пророцтво", ["те, що шукаєш, шукає тебе", "усе минеться", "відповідь у твоєму серці"])
    if st.button("Гроші/Робота", disabled=is_disabled):
        show_prediction("Гроші", ["очікуй прибутку", "краще не ризикуй", "час інвестувати в себе"])
    if st.button("Наскільки?", disabled=is_disabled):
        show_prediction("Наскільки", ["1", "10", "50", "100", "1000"])

if st.button("Мій настрій", disabled=is_disabled):
    show_prediction("Настрій", ["ти тигр", "ти сонна булочка", "ти ракета"])
