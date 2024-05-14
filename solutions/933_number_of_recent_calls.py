class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        #base case
        if len(self.requests) <= 1:
            return 1
            
        num_requests = 0
        for i in self.requests[::-1]:
            if t - i <= 3000: 
                num_requests += 1
        return num_requests


        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
