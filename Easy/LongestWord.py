# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.
def LongestWord(sen):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in punctuation:
        sen = sen.replace(char, '')  # Remove each character in punctuation from the string

    words = sen.split()  # Split the string into words

    longest_word = max(words, key=len)  # Find the longest word using the max function

    return longest_word

# Example usage:
sen = "Hello, this is a sample string! It includes various words."
print(LongestWord(sen))
