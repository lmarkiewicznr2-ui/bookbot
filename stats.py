def get_num_words(text):
    words = text.split()
    return len(words)



def get_char_counts(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts
def sort_char_counts(char_dict):
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]

    def get_num(entry):
        return entry["num"]
    char_list.sort(key=get_num, reverse=True)
    return char_list