# core/quantum_leap.py
from transformers import pipeline
from keybert import KeyBERT
from collections import Counter
import numpy as np

class QuantumLeapAnalyzer:
    """An advanced AI-powered analyzer that can handle long documents via chunking."""

    def __init__(self):
        print("Loading AI models... (This may take a moment)")
        self.sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        self.summarizer = pipeline("summarization", model="t5-small")
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
        self.kw_model = KeyBERT()
        print("Models loaded successfully!")

    def _chunk_text(self, text: str, chunk_size: int = 350):
        """Splits a long text into smaller chunks based on word count."""
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunks.append(" ".join(words[i:i + chunk_size]))
        return chunks

    def analyze(self, text: str):
        """Analyzes text by processing it in chunks and aggregating results."""
        chunks = self._chunk_text(text)
        
        # --- Sentiment Analysis (Aggregated) ---
        all_sentiments = self.sentiment_pipeline(chunks)
        # Convert sentiment to a number (e.g., POSITIVE -> 1, NEGATIVE -> -1) and average the scores
        sentiment_scores = [result['score'] if result['label'] == 'POSITIVE' else -result['score'] for result in all_sentiments]
        avg_sentiment_score = np.mean(sentiment_scores)
        
        final_sentiment_label = "Positive" if avg_sentiment_score > 0 else "Negative"
        final_confidence = f"{abs(avg_sentiment_score):.2%}"

        # --- Summarization (Hierarchical) ---
        # First, summarize each chunk individually
        chunk_summaries = []
        for chunk in chunks:
            # T5-small needs a minimum length, so we only summarize chunks that are long enough
            if len(chunk.split()) > 40:
                summary_result = self.summarizer(chunk, max_length=100, min_length=20, do_sample=False)
                chunk_summaries.append(summary_result[0]['summary_text'])
        
        # Then, summarize the combined summaries to get a final summary
        final_summary = "Text is too short or too fragmented to summarize effectively."
        if chunk_summaries:
            combined_summary = " ".join(chunk_summaries)
            if len(combined_summary.split()) > 50:
                final_summary_result = self.summarizer(combined_summary, max_length=150, min_length=40, do_sample=False)
                final_summary = final_summary_result[0]['summary_text']

        return {
            "analyzer": "AI-Powered (Chunked Analysis)",
            "sentiment": f"{final_sentiment_label} (Avg. Confidence: {final_confidence})",
            "summary": final_summary,
            "details": f"Processed {len(chunks)} text chunks to provide this analysis."
        }

    def get_keywords(self, text: str, num_keywords: int = 5):
        """Extracts keywords from all chunks and finds the most frequent ones."""
        chunks = self._chunk_text(text)
        all_keywords = []
        for chunk in chunks:
            # Extract keywords from each chunk
            keywords = self.kw_model.extract_keywords(chunk, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=num_keywords)
            all_keywords.extend([kw for kw, score in keywords])
        
        # Find the most common keywords across all chunks
        most_common_keywords = [kw for kw, count in Counter(all_keywords).most_common(num_keywords)]
        return most_common_keywords

    def answer_question(self, context: str, question: str):
        """Finds the best answer by searching through all chunks."""
        chunks = self._chunk_text(context)
        best_answer = ""
        highest_score = 0.0
        
        for chunk in chunks:
            try:
                qa_result = self.qa_pipeline(question=question, context=chunk)
                if qa_result['score'] > highest_score:
                    highest_score = qa_result['score']
                    best_answer = qa_result['answer']
            except Exception:
                # Ignore chunks that are too long for the QA model
                continue
        
        if not best_answer:
            return "Could not determine an answer from the provided text."
        
        return best_answer

    def get_entities(self, text: str):
        """Identifies named entities (People, Orgs, Locations) in the text."""
        # Use a dedicated NER pipeline
        ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)
        
        # Process text in chunks to avoid token limit issues
        chunks = self._chunk_text(text, chunk_size=400) # Use smaller chunks for NER
        all_entities = []
        
        for chunk in chunks:
            entities = ner_pipeline(chunk)
            all_entities.extend(entities)

        # Group entities by type for cleaner display
        grouped_entities = {'PER': [], 'ORG': [], 'LOC': [], 'MISC': []}
        for entity in all_entities:
            entity_type = entity['entity_group']
            entity_name = entity['word']
            if entity_name not in grouped_entities[entity_type]:
                grouped_entities[entity_type].append(entity_name)
                
        return grouped_entities