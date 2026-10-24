class Solution:

  def gcdOfStrings(self, str1, str2):
    # Check if they have a common pattern
    if str1 + str2 != str2 + str1:
      return ""

    # Inline Euclidean algorithm to find the GCD of lengths
    a, b = len(str1), len(str2)
    while b:
      a, b = b, a % b

    # Return the prefix of the calculated GCD length (a)
    return str1[:a]
