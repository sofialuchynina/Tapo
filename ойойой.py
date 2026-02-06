import streamlit as st
import random

# Налаштування сторінки
st.set_page_config(page_title="SLV")

# Оновлений CSS (без емодзі)
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
    
    /* ЗМІНА: Колір тексту над полем введення */
    .stTextInput label {
        color: #000000 !important;
        font-weight: bold;
    }
    
    /* ЗМІНА: Чорний текст самого введення (те, що ти пишеш) */
    input {
        color: ##FFFFFF !important;
    }
    
    /* Колір підказки (placeholder) */
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
    
    div.stButton > button:hover {
        background-color: #FFB6C1 !important;
        border-color: #D02090 !important;
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
    if st.button("Кохання/Дружба"):
        show_prediction("Про любов", ["кохання", "френдзона", "пішов він нахуй"])
    if st.button("Коли це буде?"):
        show_prediction("Час", ["дууууууже скоро (1-2 дні)", "дуже скоро (1-2 тижні)", "скоро (1-2 місяці)", "ще не визначено", "ну піздєц"])
    if st.button("Порада дня"):
        show_prediction("Порада", ["будь уважним до деталей", "довіряй інтуїції", "зроби паузу і відпочинь"])
    if st.button("Пачіму?"):
        show_prediction("Пачіму", ["бо даун", "бо красавчік"])

with col2:
    if st.button("Так чи Ні?"):
        show_prediction("Відповідь", ["так", "ні"])
    if st.button("Пророцтво"):
        show_prediction("Пророцтво", ["те, що шукаєш, шукає тебе", "усе минеться", "відповідь у твоєму серці"])
    if st.button("Гроші/Робота"):
        show_prediction("Гроші", ["очікуй прибутку", "краще не ризикуй", "час інвестувати в себе"])
    if st.button("Наскільки?"):
        show_prediction("Наскільки", ["1", "10", "50", "100", "1000"])

if st.button("Мій настрій"):
    show_prediction("Настрій", ["ти тигр", "ти сонна булочка", "ти ракета"])