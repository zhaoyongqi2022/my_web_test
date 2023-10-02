import streamlit as st

# Title
st.title("My Streamlit Web App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.write("Welcome to my Streamlit web app!")

# Adding data to the web app
data = [1, 2, 3, 4, 5]
st.write("Here is some data:")
st.write(data)

# Displaying a plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x ** 2

st.write("Here is a simple plot:")
st.line_chart({'x': x, 'y': y})

# Interactive widgets
st.sidebar.header("Interactive Widgets")

# Slider
slider_value = st.sidebar.slider("Select a value", 0, 100, 50)

# Button
if st.sidebar.button("Click Me"):
    st.sidebar.write(f"You selected: {slider_value}")

# Checkboxes
options = st.sidebar.checkbox("Show data", True)
if options:
    st.write("Data is shown.")

# Text input
user_input = st.text_input("Enter your name", "John Doe")
st.write(f"Hello, {user_input}!")

# Run the app
if __name__ == '__main__':
    st.sidebar.text("This is a sidebar")
