class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Min ways delete all, insert all
        ptr1 = len(word1)-1
        ptr2 = len(word2)-1
        memo = dict()
        def minDistancePtr(ptr1, ptr2):
            if ptr1<0:
                return ptr2
            if ptr2 <0:
                return ptr1
            if word1[ptr1] == word2[ptr2] :
                if not memo.get((ptr1-1, ptr2-1)) :
                    memo[(ptr1-1, ptr2-1)] = minDistancePtr( ptr1-1, ptr2-1)
                return memo[(ptr1-1, ptr2-1)]
            else:
                if not memo.get((ptr1, ptr2-1)) :
                    memo[(ptr1, ptr2-1)] = minDistancePtr( ptr1, ptr2-1)
                if not memo.get((ptr1-1, ptr2-1)) :
                    memo[(ptr1-1, ptr2-1)] = minDistancePtr( ptr1-1, ptr2-1)
                if not memo.get((ptr1-1, ptr2)) :
                    memo[(ptr1-1, ptr2)] = minDistancePtr( ptr1-1, ptr2)
                return 1 + min(memo[ (ptr1, ptr2-1)], memo[(ptr1-1, ptr2)],memo[ (ptr1-1, ptr2-1) ] )
        return 1 + minDistancePtr(ptr1, ptr2)