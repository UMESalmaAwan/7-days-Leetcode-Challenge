class Solution:
    def numberOfBeams(self, bank):
        n,m = len(bank),len(bank[0])
        val = []
        for i in range(n):
            countt = 0
            for j in range(m):
                if(bank[i][j] == '1'):
                    countt+=1
            if countt != 0:
                val.append(countt)
                
        n = 0  
        k = len(val) - 1
        for v in range(k):
            n += val[v] * val[v+1]
        
        return n