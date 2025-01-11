import streamlit as st

def main():
    st.title("Streamlit Template")
    st.header("Welcome to Streamlit!")
    st.subheader("This is a basic template.")
    
    st.text("This is some text.")
    st.markdown("**This is markdown text.**")
    
    st.write("You can write normal text with st.write.")
    
    if st.button("Say hi"):
        st.write("Hi there!")
    else:
        st.write("Goodbye")
    
    name = st.text_input("Masukkan namamu:")
    if name:
        st.write(f"Hello, {name}!")
    
    age = st.slider("Select your age:", 0, 100, 15)
    st.write(f"Your age is: {age}")
    
    st.sidebar.title("Sidebar")
    st.sidebar.write("This is the sidebar.")
    
    option = st.sidebar.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])
    st.sidebar.write(f"You selected: {option}")

if __name__ == "__main__":
    main()