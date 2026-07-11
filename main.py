import streamlit as st

st.logo("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fc8.alamy.com%2Fcomp%2F2WRAHCM%2Fgolden-avatar-icon-golden-profile-icon-2WRAHCM.jpg&f=1&nofb=1&ipt=0cf7ba20aa1272c1c56877a34ae5a8b894bc088b69cb868ad485e0ab1ee14632", size='large')

pages = {
    "Daily life": [
        st.Page("dailyLife1.py", title = "Page 1")
    ],

    "Favorite food": [
        st.Page("food.py", title = "Food")
    ],
    "Data Analytics": [
        st.Page("dataframe.py", title = "Table")
    ],
    "Money Laundering": [
        st.Page("moneylaundering.py", title = "Legal stuff")
    ]
}

pg = st.navigation(pages)
pg.run()
