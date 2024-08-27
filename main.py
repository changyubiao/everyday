import streamlit as st

from css.style import style_str
from utils.everyday import everyday_notice, tz

st.set_page_config(
    page_title="Every Day App",  # 页面标题
    page_icon=":rainbow:",  # icon
    layout="centered",  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)


def callback():
    cur_t = tz.get_cur_datetime_str()
    print(f"callback:begin... {cur_t}", flush=True)
    return cur_t


def app(name: str):
    cur_t = tz.get_cur_datetime_str()
    print(f"app:cur_time: {cur_t}", flush=True)

    today = tz.str_to_date(cur_t)
    info = everyday_notice(today)
    st.header('Every Day App')
    st.write(f"Hi, {name}  \n\n")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Now: {cur_t}. \n\n")

    with col2:
        st.button("Update Time", on_click=callback)

    st.write(f"{info}")

    st.write(style_str, unsafe_allow_html=True)


def run():
    app("Frank ")


if __name__ == '__main__':
    run()
