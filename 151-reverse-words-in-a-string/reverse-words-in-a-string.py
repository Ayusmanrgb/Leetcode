class Solution:

  def reverseWords(self, s):
    # Split by whitespace to filter out empty strings automatically
    words = s.split()
    # Reverse the order of the words
    words.reverse()
    # Join the words with a single space
    return " ".join(words)
