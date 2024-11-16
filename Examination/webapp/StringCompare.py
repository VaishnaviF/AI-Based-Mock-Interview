from nltk.metrics import jaccard_distance
import re
def jaccard_similarity(str1, str2):
    pattern = r'[^a-zA-Z0-9\s]'
    str1 = re.sub(pattern, ' ', str1)
    str2 = re.sub(pattern, ' ', str2)
    
    str1=str1.lower()

    str2=str2.lower()
    # Tokenize the strings into sets of words
    words1 = set(str1.split())
    words2 = set(str2.split())
    print(words1, words2,'<<<<<<<<<<<<')

    # Calculate Jaccard similarity using the Jaccard distance
    try:distance = jaccard_distance(words1, words2)
    except ZeroDivisionError as e:distance=1

    # Similarity is 1 - distance
    similarity = 1 - distance
    #print(words1, words2,'<<<<<<<<<<<<',similarity)
    return similarity


if __name__ == '__main__':
    string1 = "Yes Python is case-sensitive."
    string2 = "yes Python is case sensitive"

    similarity_score = jaccard_similarity(string1, string2)
    print(f"Jaccard Similarity: {similarity_score}")
