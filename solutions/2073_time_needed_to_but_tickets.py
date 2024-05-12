class Solution:
    ## Solution run time is O(n * m)
    ## In the worst case you iteratre through the entire tickts list n times.
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i]:
                    tickets[i] -= 1
                    time += 1
                if (i == k and tickets[k] == 0): 
                    return time
