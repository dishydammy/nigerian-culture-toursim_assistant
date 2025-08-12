import streamlit as st

def main():
    st.set_page_config(page_title="🇳🇬 Nigerian Culture & Tourism Assistant", layout="centered")
    st.title("🇳🇬 Nigerian Culture & Tourism Assistant (Alpha)")
    st.write("Welcome! Ask about states, festivals, food, or places to visit.")
    q = st.text_input("Ask a question about Nigeria:")
    if q:
        st.info("RAG not connected yet — this is a placeholder response.")
        st.write(f"You asked: {q}")

if __name__ == "__main__":
    main()
