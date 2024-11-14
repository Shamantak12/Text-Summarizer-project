from .summarizer import TextSummarizer
from .analyzer import TextAnalyzer
from .preprocessor import TextPreprocessor
from .utils import load_config, save_results


__version__ = "0.1.0"


__all__ = ["TextSummarizer", "TextAnalyzer", "TextPreprocessor", "load_config", "save_results"]


config = load_config()


summarizer = TextSummarizer(config)
analyzer = TextAnalyzer(config)
preprocessor = TextPreprocessor(config)


def summarize_and_analyze(text):
    preprocessed_text = preprocessor.preprocess(text)
    summary = summarizer.summarize(preprocessed_text)
    analysis = analyzer.analyze(summary)
    save_results(summary, analysis)
    return summary, analysis


print(f"Package initialized successfully with version {__version__}")