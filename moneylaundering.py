import streamlit as st

import pandas as pd
import numpy as np

df = pd.DataFrame({
  'first column': [1,2,3,4],
  'second column': [10,20,30,40],
})

df

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# dataframe = pd.DataFrame(
#   np.random.randn(10, 20),
#   columns= ('col %d' % i for i in range(20))
# )

# st.dataframe(dataframe.style.highlight_max(axis=0))


# product_data = {
#     "Product": [
#         ":material/devices: Widget Pro",
#         ":material/smart_toy: Smart Device",
#         ":material/inventory: Premium Kit",
#     ],
#     "Category": [":blue[Electronics]", ":green[IoT]", ":violet[Bundle]"],
#     "Stock": ["🟢 Full", "🟡 Low", "🔴 Empty"],
#     "Units sold": [1247, 892, 654],
#     "Revenue": [125000, 89000, 98000],
# }

# st.table(product_data, border=True)

##Line chart

# chart_data = pd.DataFrame(
#   np.random.randn(20, 3),
#   columns = ['a', 'b', 'c']
# )

# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#   np.random.randn(1000, 2) / [50, 50] + [43.65, -79.38],
#   columns = ['lat', 'lon']
# )

# st.map(map_data)

##[37.76, -122.4] san francisco

# x = st.slider('x')
# st.write(x, 'plus 2 is', x+2)

# Text input field
st.text_input("Your name", key="name")
st.text_input("Your city", key="city")
st.session_state.name
st.session_state.city


# Checkbox
if st.checkbox('Show dataframe'):
  chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['Col1', 'Col2', 'Col3']
  )

  chart_data

#SelectBox

df = pd.DataFrame({
  'first column': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
  'second column': [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
})

option = st.selectbox(
  'which number do you like best?',
  df['second column']
)

'I am in Grade', option

# using columns for layout

left_column, right_column = st.columns(2)
left_column.button('press me!')

with right_column:
    option = st.radio(
        'Choosing colours',
        ('red', 'green', 'blue', 'yellow')
    )

    st.write(f'You have chosen the colour {option}!')

    import time, random

    'Starting a long computation...'

    latest_iteration = st.empty()
    i = 0
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration {(i + 1)} at {(i + 1)}%...')
        bar.progress(i + 1)
        time.sleep(random.randint(1, 3000) / 1000)
        if i < 80:
            'Still going...'
        else:
            'Finishing up...'
    'And...now we are finished!'