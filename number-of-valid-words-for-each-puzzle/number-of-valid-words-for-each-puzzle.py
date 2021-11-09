class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        #Read leetcode slon for good understanding
        def bitmask(word):
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            return mask

        # Create a bitmask for each word.
        word_count = Counter(bitmask(word) for word in words)

        result = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            count = word_count[first]

            # Make bitmask but ignore the first character since it must always
            # be there.
            mask = bitmask(puzzle[1:])

            # Iterate over every possible subset of characters.
            submask = mask
            while submask:
                # Increment the count by the number of words that match the
                # current submask.
                count += word_count[submask | first]  # add first character
                submask = (submask - 1) & mask
            result.append(count)
        return result
                
                