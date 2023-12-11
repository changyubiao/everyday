import streamlit as st
from utils.everyday import everyday_notice, get_cur_time


st.set_page_config(
    page_title="Every Day App",  # 页面标题
    page_icon=":rainbow:",  # icon
    layout="centered",  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)


def callback():
    print("callback begin...")
    cur_t = get_cur_time()
    return cur_t


def app(name):
    info = everyday_notice()
    cur_t = get_cur_time()
    st.header('Every Day App')
    st.write(f"Hi, {name}  \n\n")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Now: {cur_t}. \n\n")
    st.write(
        """<style>
                .st-emotion-cache-keje6w  {
                    width: calc(50% - 1rem);
                    flex: 1 1 calc(50% - 1rem);
                    display: flex;
                    align-items: center;
                    # border: 1px solid rgba(49, 51, 63, 0.2);
                    # border-radius: 4px;
                }
                
                /* button 大小 位置 */
                button.ef3psqc12 {
                    width : 150px;
                    /* margin-left: 15px; */
    
                }
            </style>
        
        """,unsafe_allow_html=True)

    with col2:
        st.button("Update Time", on_click=callback)

    st.write(f"{info}")


def run():
    app("Frank ")


if __name__ == '__main__':
    run()
