class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        sorted_citations = sorted(citations)
        h = 1
        for index, element in enumerate(sorted_citations):
            print("Element: ", element)
            print("size - index: ", size - index)
            if element <= size - index:
                h = element
            else: 
                h = max(h, size - index)
        return h
