def longest_word(sen) :
    words = sen.split()
    print("Converted into array of strings , we will go each index now and check the length of the word")
    print(words)
    longest = ""
    for word in words:
        print(word)
        print("The length of word ->" , len(word))
        print("The length of longest ->" , len(longest))
        if len(word) > len(longest):
            longest = word
    return longest

sentence = "The quick brown fox jumps over the lazy dog"
print("The longest word is -> ",longest_word(sentence))