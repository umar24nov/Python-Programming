def convert(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    
    # Use a set to remove duplicate words (sets automatically discard duplicates)
    unique_words = set(words)
    
    # Sort the unique words alphanumerically
    sorted_words = sorted(unique_words)
    
    # Join the sorted words back into a single string separated by spaces
    result = " ".join(sorted_words)
    
    return result


input_sentence = """Sakhi was a singer because her mother was a singer and Sakhi's mother
was a singer because her father was a singer"""
output_sentence = convert(input_sentence)

print(f"Output: {output_sentence}")
