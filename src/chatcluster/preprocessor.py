from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from spellchecker import SpellChecker
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import re
import torch
import pandas as pd

class UserMessagesPreprocessor:
    def __init__(self, messages: list[str]):
        self._processed_df = self._preprocess(messages)

    def get_df(self) -> pd.DataFrame:
        return self._processed_df

    def _preprocess(self, messages: list[str]) -> pd.DataFrame:
        total_messages = len(messages)

        total_words = self._get_total_words(messages)
        total_reformulations = self._get_total_reformulations(messages)
        total_spelling_errors = self._get_total_spelling_errors(messages)
        total_questions = self._get_total_questions(messages)
        neutral_count, positive_count, negative_count = self._get_sentiment_count(messages)

        def _norm(x: float) -> float:
            return round(x / total_messages, 6) if total_messages > 0 else 0.0

        data = {
            "neutral_count": _norm(neutral_count),
            "positive_count": _norm(positive_count),
            "negative_count": _norm(negative_count),
            "total_reformulations": _norm(total_reformulations),
            "total_words": _norm(total_words),
            "total_spelling_errors": _norm(total_spelling_errors),
            "total_questions": _norm(total_questions),
        }
        return pd.DataFrame([data])

    @staticmethod
    def _get_sentiment_count(messages: list[str]) -> (float, float, float):
        analyzer = SentimentIntensityAnalyzer()

        neutral = positive = negative = 0

        for msg in messages:
            if not isinstance(msg, str) or not msg.strip():
                neutral += 1
                continue
            scores = analyzer.polarity_scores(msg)
            compound = scores['compound']
            if compound >= 0.05:
                positive += 1
            elif compound <= -0.05:
                negative += 1
            else:
                neutral += 1

        return float(neutral), float(positive), float(negative)

    @staticmethod
    def _get_total_reformulations(messages: list[str]) -> float:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = SentenceTransformer(
            'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
            device=device
        )

        messages = [msg for msg in messages if isinstance(msg, str) and msg.strip()]
        if len(messages) < 2:
            return 0.0

        embeddings = model.encode(messages, convert_to_tensor=False, device=device)
        sims = cosine_similarity(embeddings[:-1], embeddings[1:])
        count = sum(1 for sim in sims.diagonal() if 0.8 <= sim < 0.99)

        return float(count)

    @staticmethod
    def _get_total_spelling_errors(messages: list[str]) -> float:
        spell = SpellChecker()

        total_errors = 0
        for msg in messages:
            if not isinstance(msg, str):
                continue
            words = re.findall(r'\b[a-zA-Z]{2,}\b', msg.lower())
            misspelled = spell.unknown(words)
            total_errors += len(misspelled)
        return float(total_errors)

    @staticmethod
    def _get_total_questions(messages: list[str]) -> float:
        return float(sum(msg.count('?') for msg in messages if msg))

    @staticmethod
    def _get_total_words(messages: list[str]) -> float:
        def count_words(text: str) -> int:
            return len(text.strip().split())

        count = 0
        for msg in messages:
            count += count_words(msg)

        return float(count)
