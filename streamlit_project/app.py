# Exercise 1: Text and Data Display
import streamlit as st  # Importing the Streamlit library

# Basic text elements
st.title("My First Streamlit App")  # Adds a big title at the top of the app
# Adds a section header — good for breaking content into parts
st.header("Section 1")
st.subheader("Header")  # Slightly smaller than header — useful for structure
st.subheader("Subheader")  # Another level down — keeps things organized
# Displays plain, unformatted text — like a basic message
st.text("Simple text")
# Markdown lets you add simple formatting like bold and italics
st.markdown("**Bold** and *italic* text")

# Display data
# Streamlit's flexible method — handles strings, numbers, dataframes, and more
st.write("Automatic data display")
# Nicely formats code blocks with syntax highlighting
st.code("print('Hello World')", language='python')
# Renders LaTeX math formulas — great for equations
st.latex(r"\int_{a}^{b} x^2 dx")

# Exercise - 2: Data Input Components
# Text input
st.header("Section 2")  # A new section to group interactive input components
# Simple text field with a default value
name = st.text_input("Enter your name", "John Doe")
# Multi-line text box for longer input
description = st.text_area("Description", "Write something...")

# Numeric input
age = st.number_input("Age", min_value=0, max_value=120,
                      value=25)  # Number picker with min/max range
# Slider to pick a number in a range — great for ratings or scores
score = st.slider("Score", 0, 100, 50)

# Selection widgets
# Dropdown menu — user picks one option
option = st.selectbox("Choose an option", ["A", "B", "C"])
# Allows multiple selections at once
options = st.multiselect("Multiple options", ["X", "Y", "Z"])

# Date and time
date = st.date_input("Select date")  # Calendar-style date picker
time = st.time_input("Select time")  # Clock-style time picker

# Buttons and checkbox
if st.button("Click me"):  # A button that runs code when clicked
    st.write("Button clicked!")  # Responds when the button is pressed

if st.checkbox("Show/Hide"):  # Checkbox to toggle something on/off
    # Displays this text only if the box is checked
    st.write("Visible content")

# Exercise 3: Layout and Containers
st.header("Section 3")

# Create two side-by-side columns
col1, col2 = st.columns(2)

with col1:  # Everything under this goes into the left column
    st.header("Column 1")
    st.write("Content for column 1")

with col2:  # Everything under this goes into the right column
    st.header("Column 2")
    st.write("Content for column 2")

# Expandable sections
with st.expander("Click to expand"):
    st.write("Expanded content here")

# Sidebar
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])
