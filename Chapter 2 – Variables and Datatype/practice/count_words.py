def count_words(string) :
    words = string.split()
    return len(words)

sentence = "rahul is a good boy" #5
print("The number of words in the sentence are ->",count_words(sentence))