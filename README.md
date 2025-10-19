# 🚀 QuantumLeap AI: A Conceptual Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://quantum-leap-ai.streamlit.app/) <!-- IMPORTANT: Replace this URL with your actual app URL! -->

An interactive web application that demonstrates the monumental difference between traditional, rule-based programming and modern, state-of-the-art artificial intelligence.

By analyzing the same text with two fundamentally different methods side-by-side, this project makes the abstract concept of a "quantum leap" in technology tangible and easy to understand.

![Demo GIF of the App](https://your-gif-url-here.gif) <!-- IMPORTANT: Add a screenshot or a GIF of your app here! -->

## ✨ The "Quantum Leap" in Action

The application analyzes any given text using two distinct paradigms:

### ⚙️ Old State
A simple, rule-based system that relies on basic keyword counting. It's fast but lacks any real understanding of context, nuance, or meaning.

### ✨ Quantum Leap
A powerful, AI-powered system that leverages massive, pre-trained Transformer models from Hugging Face. It performs deep, contextual analysis to provide truly intelligent insights.

## 🛠️ Core Features

-   **📝 Sentiment Analysis:** Gauges the emotional tone of the text.
-   **📄 Summarization:** Condenses long articles (1000+ words) into a concise summary using advanced chunking.
-   **🔑 Keyword Extraction:** Identifies the most important topics and keyphrases.
-   **🤖 Question Answering:** Answers direct questions based on the provided text.
-   **🏷️ Named Entity Recognition (NER):** Identifies and tags People, Organizations, and Locations.
-   **🔊 Text-to-Speech:** Reads the AI-generated summary out loud.
-   **✍️ Text Generation:** Creatively continues a story or document.
-   **🌍 Multi-Language Support:** Full UI support for English and Bangla.
-   **📚 Genre Library:** Pre-loaded with 1000-word sample texts from various genres (Essay, Drama, Sci-Fi, etc.).

## 🛠️ Tech Stack

-   **Frontend:** [Streamlit](https://streamlit.io/)
-   **Backend:** [Python](https://www.python.org/)
-   **AI Models:** [Hugging Face Transformers](https://huggingface.co/transformers/)
-   **Keyword Extraction:** [KeyBERT](https://github.com/MaartenGr/KeyBERT)
-   **Text-to-Speech:** [gTTS](https://pypi.org/project/gTTS/)

## 🚀 Live Demo

Check out the live application here: **[https://your-app-url-here.streamlit.app](https://quantum-leap-ai.streamlit.app/)**

## 📋 How to Run Locally

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/quantum-leap-ai.git
    cd quantum-leap-ai
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS / Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

Your web browser should automatically open to `http://localhost:8501`.

## 📁 Project Structure
