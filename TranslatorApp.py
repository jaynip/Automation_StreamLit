import streamlit as st
from googletrans import LANGUAGES, Translator

def main():
    st.title("Language Translator App")
    st.write("This app translates entered text from one language to another.")
    
    text_input = st.text_area("Enter text to translate", placeholder="Enter text to translate..")
    
    languages = get_lang()
    
    # select a target language
    target_lang = st.selectbox("Select translated language", languages.values())  # Use language codes
    btn = st.button("Translate")

    if btn:
        if text_input:
            try:
                translation = translate_text(text_input, target_lang)
                st.subheader("Translated Text:")
                st.write(translation)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter valid text to translate.")
        
def get_lang():
    return LANGUAGES

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

if __name__ == "__main__":
    main()
