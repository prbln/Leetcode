class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = dict()
        for ele in s:
            hashmap[ele] = hashmap.get(ele,0) +1
        print(hashmap)
        s= sorted(s)
        return ('').join(sorted(s , key = lambda x : hashmap[x], reverse = True ))