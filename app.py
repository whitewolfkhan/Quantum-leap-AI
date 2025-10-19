# app.py
import streamlit as st
from core.old_state import SimpleAnalyzer
from core.quantum_leap import QuantumLeapAnalyzer
from lang import EN, BN
from sample_texts import SAMPLE_TEXTS # Import the new sample texts

# --- Helper Function for Translations ---
def get_text(lang_code):
    """Returns the correct translation dictionary."""
    return EN if lang_code == 'EN' else BN

# --- Session State Initialization ---
if 'lang' not in st.session_state:
    st.session_state.lang = 'EN'

# --- Language Selector in Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    st.session_state.lang = st.selectbox(
        "Choose Language / ভাষা নির্বাচন করুন:",
        ('EN', 'BN'),
        index=0 if st.session_state.lang == 'EN' else 1
    )

texts = get_text(st.session_state.lang)

# --- Page Configuration ---
st.set_page_config(
    page_title=texts["app_title"],
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Main App UI ---
st.title(f"🚀 {texts['app_title']}")
st.markdown(texts['app_intro'])
st.markdown(f"1. **{texts['old_state_title']}** {texts['old_state_desc']}")
st.markdown(f"2. **{texts['quantum_leap_title']}** {texts['quantum_leap_desc']}")

# --- User Input (with genre selector) ---
with st.sidebar:
    st.header("📄 Sample Text")
    selected_genre = st.selectbox(
        texts["sample_text_label"],
        list(SAMPLE_TEXTS.keys())
    )
    # The text area now uses the selected genre to get the default text
    user_input = st.text_area(
        label=texts["text_input_label"],
        height=300,
        value=SAMPLE_TEXTS[selected_genre]
    )

# --- The rest of the app.py file remains the same ---
# (The analyze buttons, columns, and advanced analysis sections don't need to change)

if st.button(texts["analyze_button"]):
    if not user_input:
        st.warning(texts["warning_no_text"])
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.header("⚙️ " + texts["old_state_title"].strip(":"))
            simple_analyzer = SimpleAnalyzer()
            simple_result = simple_analyzer.analyze(user_input)
            st.info(simple_result["analyzer"])
            st.write(f"**Word Count:** {simple_result['word_count']}")
            st.write(f"**Sentiment:** {simple_result['sentiment']}")
            st.caption(simple_result["details"])

        with col2:
            st.header("✨ " + texts["quantum_leap_title"].strip(":"))
            with st.spinner("Performing AI analysis on long text... This may take longer."):
                ai_analyzer = QuantumLeapAnalyzer()
                ai_result = ai_analyzer.analyze(user_input)
            st.success(ai_result["analyzer"])
            st.write(f"**Sentiment:** {ai_result['sentiment']}")
            st.write("**Summary:**")
            st.write(ai_result["summary"])
            st.caption(ai_result["details"])

# --- New Advanced Analysis Section ---
st.markdown("---")
st.header(texts["advanced_analysis_header"])

# --- Keyword Extraction ---
st.subheader(texts["keyword_extraction_header"])
st.write(texts["keyword_extraction_desc"])

if st.button(texts["extract_keywords_button"]):
    if not user_input:
        st.warning(texts["warning_no_text"])
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.header("⚙️ " + texts["old_state_title"].strip(":"))
            simple_analyzer = SimpleAnalyzer()
            simple_keywords = simple_analyzer.get_keywords(user_input)
            st.info("Most Frequent Words")
            st.write(", ".join(simple_keywords))

        with col2:
            st.header("✨ " + texts["quantum_leap_title"].strip(":"))
            with st.spinner("Performing AI keyword extraction on long text..."):
                ai_analyzer = QuantumLeapAnalyzer()
                ai_keywords = ai_analyzer.get_keywords(user_input)
            st.success("AI-Powered Keyphrases")
            st.write(", ".join(ai_keywords))

# --- Question Answering ---
st.subheader(texts["qa_header"])
st.write(texts["qa_desc"])

user_question = st.text_input(
    label=texts["qa_input_label"],
    value="What is the main topic of this text?"
)

if st.button(texts["ask_question_button"]):
    if not user_input or not user_question:
        st.warning(texts["warning_no_text_or_question"])
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.header("⚙️ " + texts["old_state_title"].strip(":"))
            simple_analyzer = SimpleAnalyzer()
            simple_answer = simple_analyzer.answer_question(user_input, user_question)
            st.info("Keyword Search Result")
            st.write(simple_answer)

        with col2:
            st.header("✨ " + texts["quantum_leap_title"].strip(":"))
            with st.spinner("Performing AI question answering on long text..."):
                ai_analyzer = QuantumLeapAnalyzer()
                ai_answer = ai_analyzer.answer_question(user_input, user_question)
            st.success("AI-Generated Answer")
            st.write(ai_answer)
      
      
      
# ... (keep the rest of app.py the same) ...

# --- Named Entity Recognition ---
st.subheader(texts["ner_header"])
st.write(texts["ner_desc"])

if st.button(texts["extract_entities_button"]):
    if not user_input:
        st.warning(texts["warning_no_text"])
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.header("⚙️ " + texts["old_state_title"].strip(":"))
            st.info("No capability")
            st.write("The simple analyzer cannot identify entities. It only sees words.")

        with col2:
            st.header("✨ " + texts["quantum_leap_title"].strip(":"))
            with st.spinner("Performing AI entity extraction..."):
                ai_analyzer = QuantumLeapAnalyzer()
                ai_entities = ai_analyzer.get_entities(user_input)
            
            st.success("AI-Powered Entities")
            
            # Display the results in a clean format
            if ai_entities['PER']:
                st.write(f"**{texts['people_label']}:**")
                st.write(", ".join(ai_entities['PER']))
            if ai_entities['ORG']:
                st.write(f"**{texts['orgs_label']}:**")
                st.write(", ".join(ai_entities['ORG']))
            if ai_entities['LOC']:
                st.write(f"**{texts['locs_label']}:**")
                st.write(", ".join(ai_entities['LOC']))
            if ai_entities['MISC']:
                st.write(f"**{texts['misc_label']}:**")
                st.write(", ".join(ai_entities['MISC']))      
            