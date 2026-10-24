class Solution:

  def mergeAlternately(self, word1, word2):
    merged = []
    for i in range(max(len(word1), len(word2))):
      if i < len(word1):
        merged.append(word1[i])
      if i < len(word2):
        merged.append(word2[i])
    return "".join(merged)
