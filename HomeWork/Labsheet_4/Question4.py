def frequency(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Create a dictionary to store word frequencies
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
            
    # Sort the dictionary by keys (words) and convert it to a list of tuples
    sorted_freq = sorted(freq_dict.items())
    
    return sorted_freq


input_string = "This is a test string. This string is just a test."
result = frequency(input_string)


for word, freq in result:
    print(f"{word} : {freq}")
