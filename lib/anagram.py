# your code goes here!
class Anagram:
    def __init__(self, word):
        # Initialize the object with a sorted list of letters from the input word
        self.word_letters = sorted(word)

    def match(self, word_list):
        match_word_list = []

        # Iterate through each word in the word list
        for word in word_list:
            # Sort the letters of the current word and compare with the sorted letters of the input word
            if sorted(word) == self.word_letters:
                # If the sorted letters match, it's an anagram, so add it to the match_word_list
                match_word_list.append(word)

        # Return the list of matching anagrams
        return match_word_list