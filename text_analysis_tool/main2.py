
import argparse
import re
from collections import Counter

def read_files(file_paths):
    """Read and combine text from all input files."""
    all_text = ""
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            all_text += f.read() + " "
    return all_text

def clean_and_tokenize(text):
    """Clean text and return a list of lowercase words."""
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    return words

def split_sentences(text):
    """Split text into sentences using punctuation."""
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return [s.strip() for s in sentences if s]

def analyze_text(text):
    words = clean_and_tokenize(text)
    sentences = split_sentences(text)
    
    # Word stats
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(10)
    unique_words = set(words)

    # Sentence stats
    longest_sentence = max(sentences, key=len)
    shortest_sentence = min(sentences, key=len)

    return most_common_words, len(unique_words), longest_sentence, shortest_sentence

def main():
    parser = argparse.ArgumentParser(description="Analyze text files for words and sentences.")
    parser.add_argument('files', nargs='+', help="Paths to text files")
    args = parser.parse_args()

    text = read_files(args.files)
    most_common, unique_count, longest, shortest = analyze_text(text)

    print("\nTEXT ANALYSIS RESULTS")
    print("="*40)
    print("\nTop 10 Most Frequent Words:")
    for word, count in most_common:
        print(f"{word}: {count}")

    print(f"\nTotal Unique Words: {unique_count}")
    print("\nLongest Sentence:\n", longest)
    print("\nShortest Sentence:\n", shortest)
    print("\nDone.")

if __name__ == "__main__":
    main()
