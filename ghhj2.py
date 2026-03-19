import streamlit as st

st.set_page_config(layout="wide")

# ---------- SESSION ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
body {
    background: #0f172a;
    overflow-x: hidden;
    color: gold;
    text-align: center;
}

/* SCENE */
.scene {
    position: relative;
    height: 500px;
}

/* PLANE */
.plane {
    position: absolute;
    top: 120px;
    left: -300px;
    width: 220px;
    animation: fly 6s ease-in-out forwards;
}

/* ROPE */
.rope {
    position: absolute;
    width: 3px;
    height: 120px;
    background: gold;
    top: 200px;
    left: -200px;
    animation: fly 6s ease-in-out forwards;
}

/* GIFT */
.gift {
    position: absolute;
    top: 320px;
    left: -230px;
    width: 110px;
    cursor: pointer;
    animation: fly 6s ease-in-out forwards, swing 2s infinite ease-in-out;
}

@keyframes fly {
    0% { left: -300px; }
    100% { left: 45%; }
}

/* SWING */
@keyframes swing {
    0% { transform: rotate(5deg); }
    50% { transform: rotate(-5deg); }
    100% { transform: rotate(5deg); }
}

/* MESSAGE */
.msg {
    font-size: 40px;
    margin-top: 50px;
    animation: fadeIn 2s;
}

@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}

/* CLICKABLE TEXT */
.princy {
    font-size: 35px;
    color: gold;
    cursor: pointer;
    text-shadow: 0 0 10px gold;
    transition: 0.3s;
}
.princy:hover {
    transform: scale(1.1);
    text-shadow: 0 0 20px gold;
}

/* PANDA */
.panda {
    width: 200px;
    margin-top: 30px;
    cursor: pointer;
}

/* CARD */
.book {
    width: 320px;
    height: 420px;
    margin: auto;
    perspective: 1000px;
}

.page {
    width: 100%;
    height: 100%;
    background: #1f2937;
    border: 2px solid gold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    border-radius: 10px;
    animation: flip 1s;
}

@keyframes flip {
    from {transform: rotateY(90deg);}
    to {transform: rotateY(0);}
}

</style>
""", unsafe_allow_html=True)

# ---------- PAGE 1 ----------
if st.session_state.page == "home":

    st.markdown("""
    <div class="scene">
        <img src="https://cdn-icons-png.flaticon.com/512/744/744465.png" class="plane">
        <div class="rope"></div>
        <img src="https://cdn-icons-png.flaticon.com/512/3468/3468377.png"
             class="gift"
             onclick="document.getElementById('open').click()">
    </div>
    """, unsafe_allow_html=True)

    if st.button("hidden", key="open"):
        st.session_state.page = "message"


# ---------- PAGE 2 ----------
elif st.session_state.page == "message":

    st.markdown('<div class="msg">Happy Birthday Dear 🎉</div>', unsafe_allow_html=True)

    if st.button("✨ Happy Birthday Princy"):
        st.session_state.page = "wishes"


# ---------- PAGE 3 ----------
elif st.session_state.page == "wishes":

    st.markdown('<div class="msg">Happy Birthday Princy 🎂</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-size:25px;">May your life be full of happiness 💖</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:25px;">You are the best sister 🌸</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-size:30px; margin-top:20px;">Once again Happy Birthday Princy 💛</div>', unsafe_allow_html=True)

    st.markdown("""
    <img src="https://cdn-icons-png.flaticon.com/512/616/616408.png"
         class="panda"
         onclick="document.getElementById('panda_btn').click()">
    """, unsafe_allow_html=True)

    if st.button("hidden2", key="panda_btn"):
        st.session_state.page = "card"


# ---------- PAGE 4 ----------
elif st.session_state.page == "card":

    if "step" not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        text = "🎉 Happy Birthday 🎉"
    elif st.session_state.step == 2:
        text = "Wishing you endless happiness 💖"
    elif st.session_state.step == 3:
        text = "🥳🎂🎁✨💛"
    else:
        text = "Thank You 💛"

    st.markdown(f'<div class="book"><div class="page">{text}</div></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️"):
            if st.session_state.step > 1:
                st.session_state.step -= 1

    with col2:
        if st.button("➡️"):
            if st.session_state.step < 4:
                st.session_state.step += 1
