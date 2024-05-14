from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        #start from the oldest request and pop if it has been too long
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
