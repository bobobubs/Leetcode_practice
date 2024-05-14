class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return n
        
        players = deque(range(1, n + 1))
        while len(players) > 1:
            players.rotate(-(k-1))
            players.popleft()

        return players[0]
                
        
