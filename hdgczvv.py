import streamlit as st

st.set_page_config(page_title="Birthday Surprise", layout="wide")

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- COMMON CSS ----------
st.markdown("""
<style>
body {
    background: #0f172a;
    color: gold;
    text-align: center;
    overflow-x: hidden;
}

/* Airplane */
.plane {
    position: absolute;
    top: 40%;
    left: -300px;
    width: 250px;
    animation: fly 5s ease-in-out forwards;
}

@keyframes fly {
    0% { left: -300px; }
    100% { left: 40%; }
}

/* Gift */
.gift {
    margin-top: 350px;
    width: 120px;
}

/* Fade animation */
.fade {
    animation: fadeIn 2s ease-in;
}

@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}

/* Slide animation */
.slide {
    animation: slideUp 2s ease-in;
}

@keyframes slideUp {
    from {transform: translateY(50px); opacity:0;}
    to {transform: translateY(0); opacity:1;}
}

/* Card */
.card {
    width: 300px;
    height: 400px;
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
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- PAGE 1 (HOME) ----------
if st.session_state.page == "home":

    st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/744/744465.png" class="plane">', unsafe_allow_html=True)

    st.write("")

    if st.button("🎁 Open Gift"):
        st.session_state.page = "message"

# ---------- PAGE 2 (MESSAGE) ----------
elif st.session_state.page == "message":

    st.markdown('<div class="fade" style="font-size:40px;">Happy Birthday Dear 🎉</div>', unsafe_allow_html=True)

    if st.button("💛 Happy Birthday Princy"):
        st.session_state.page = "wishes"

# ---------- PAGE 3 (WISHES + PANDA) ----------
elif st.session_state.page == "wishes":

    st.markdown('<div class="fade" style="font-size:50px;">Happy Birthday Princy 🎂</div>', unsafe_allow_html=True)

    st.markdown('<div class="slide" style="font-size:25px;">May your life be filled with happiness 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="slide" style="font-size:25px;">You are the best sister ever 🌸</div>', unsafe_allow_html=True)

    st.markdown('<div class="slide" style="font-size:30px; margin-top:20px;">Once again, Happy Birthday Princy 💛</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("🐼 Click Panda"):
        st.session_state.page = "card"

# ---------- PAGE 4 (FINAL CARD) ----------
elif st.session_state.page == "card":

    st.markdown('<div class="fade" style="font-size:40px;">📖 Birthday Card</div>', unsafe_allow_html=True)

    if "step" not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        st.markdown('<div class="card"><div class="page">🎉 Happy Birthday 🎉</div></div>', unsafe_allow_html=True)
    elif st.session_state.step == 2:
        st.markdown('<div class="card"><div class="page">Wishing you endless happiness 💖</div></div>', unsafe_allow_html=True)
    elif st.session_state.step == 3:
        st.markdown('<div class="card"><div class="page">🥳🎂🎁✨💛</div></div>', unsafe_allow_html=True)
    elif st.session_state.step == 4:
        st.markdown('<div class="card"><div class="page">Thank You 💛</div></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Previous"):
            if st.session_state.step > 1:
                st.session_state.step -= 1

    with col2:
        if st.button("Next ➡️"):
            if st.session_state.step < 4:
                st.session_state.step += 1
