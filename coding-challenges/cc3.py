"""cc3.py
Given a list of words, return the K most
frequent words sorted by frequency (descending).
If two words have the same frequency, return
them in lexicographical order.
"""


def top_k_frequent(words: list[str], k: int) -> list[str]:
    freq_map = {}

    for word in words:
        freq_map[word] = freq_map.get(word, 0) + 1

    sorted_items = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, freq in sorted_items[:k]]
