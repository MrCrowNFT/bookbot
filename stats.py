def get_word_count(book:str):
    return len(book.split())

def get_char_count(book:str):
    book = book.lower()
    counts ={}
    for char in book:
        counts[char] = counts.get(char, 0) +1 
    return counts

def get_sorted_char_count(counts: dict[str, int]):
    sorted_list = sorted(
        [{"char": char, "count": count} for char, count in counts.items() if char.isalpha()],
        key=lambda x: x["count"],
        reverse=True
    )
    return sorted_list