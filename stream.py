import streamlit as st

st.set_page_config(layout="wide")

# ---------- STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#020617,#0f172a);
    color: gold;
    text-align: center;
}

/* fly animation */
.fly {
    animation: fly 4s ease-out forwards;
}
@keyframes fly {
    from {transform: translateX(-600px);}
    to {transform: translateX(0);}
}

/* swing gift */
.swing {
    animation: swing 2s infinite ease-in-out;
}
@keyframes swing {
    0% {transform: rotate(6deg);}
    50% {transform: rotate(-6deg);}
    100% {transform: rotate(6deg);}
}

/* fade */
.fade {
    animation: fade 2s ease-in;
}
@keyframes fade {
    from {opacity:0;}
    to {opacity:1;}
}

/* glow text */
.glow {
    font-size: 32px;
    text-shadow: 0 0 10px gold, 0 0 20px gold;
}

/* card */
.card {
    border: 2px solid gold;
    padding: 60px;
    width: 300px;
    margin: auto;
    border-radius: 15px;
    background: rgba(255,215,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------- PAGE 1 ----------
if st.session_state.page == "home":

    st.markdown("<h1 class='fade'>✈️ Birthday Surprise</h1>", unsafe_allow_html=True)

    st.markdown('<div class="fly">', unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Airplane_silhouette.png", width=220)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="swing">', unsafe_allow_html=True)
    if st.button("🎁 Open Gift"):
        st.session_state.page = "message"
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- PAGE 2 ----------
elif st.session_state.page == "message":

    st.markdown("<h1 class='fade'>Happy Birthday Dear 🎉</h1>", unsafe_allow_html=True)

    if st.button("💛 Happy Birthday Princy"):
        st.session_state.page = "wishes"

# ---------- PAGE 3 ----------
elif st.session_state.page == "wishes":

    st.markdown("<h1 class='fade'>Happy Birthday Princy 🎂</h1>", unsafe_allow_html=True)

    st.markdown("<p class='fade'>May your life be full of happiness 💖</p>", unsafe_allow_html=True)
    st.markdown("<p class='fade'>You are the best sister 🌸</p>", unsafe_allow_html=True)

    st.markdown("<div class='glow'>Once again Happy Birthday Princy 💛</div>", unsafe_allow_html=True)

    if st.button("🐼 Tap Panda"):
        st.session_state.page = "card"

# ---------- PAGE 4 ----------
elif st.session_state.page == "card":

    if "step" not in st.session_state:
        st.session_state.step = 1

    pages = [
        "🎉 Happy Birthday 🎉",
        "Wishing you endless happiness 💖",
        "🥳🎂🎁✨💛",
        "Thank You 💛"
    ]

    st.markdown(f'<div class="card">{pages[st.session_state.step-1]}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Previous"):
            if st.session_state.step > 1:
                st.session_state.step -= 1

    with col2:
        if st.button("Next ➡️"):
            if st.session_state.step < 4:
                st.session_state.step += 1
