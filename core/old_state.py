# core/old_state.py
from collections import Counter

class SimpleAnalyzer:
    """A very basic text analyzer representing the 'old state'."""

    def __init__(self):
        self.positive_words = ["good", "great", "excellent", "amazing", "love", "fantastic", "wonderful"]
        self.negative_words = ["bad", "terrible", "awful", "hate", "horrible", "worst", "sad"]

    def analyze(self, text: str):
        # ... (original analyze method remains the same)
        words = text.lower().split()
        word_count = len(words)
        
        positive_count = sum(1 for word in words if word in self.positive_words)
        negative_count = sum(1 for word in words if word in self.negative_words)
        
        if positive_count > negative_count:
            sentiment = "Positive"
        elif negative_count > positive_count:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {
            "analyzer": "Simple Keyword-Based",
            "word_count": word_count,
            "sentiment": sentiment,
            "details": f"Found {positive_count} positive and {negative_count} negative keywords."
        }

    def get_keywords(self, text: str, num_keywords: int = 5):
        """Extracts the most frequent words. Very naive."""
        words = text.lower().split()
        # A very basic stopword list to filter out common words
        stopwords = {"the", "a", "is", "in", "it", "and", "of", "to", "that", "was", "i", "for", "be"}
        filtered_words = [word for word in words if word.isalpha() and word not in stopwords]
        common_words = Counter(filtered_words).most_common(num_keywords)
        return [word for word, count in common_words]

    def answer_question(self, context: str, question: str):
        """Answers a question based on a simple keyword search."""
        question_words = set(question.lower().split())
        context_words = set(context.lower().split())
        
        # Check if a significant portion of question words are in the context
        overlap = question_words.intersection(context_words)
        
        if len(overlap) / len(question_words) > 0.5:
            return "Yes (based on keyword presence)"
        else:
            return "No (keywords not found)"