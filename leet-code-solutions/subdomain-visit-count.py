class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit = {}
        for i in cpdomains:
        
            count , domain = i.split()
            count = int(count)
            
            subdomains = domain.split('.')
            print(subdomains)
            for sub in range(len(subdomains)):
                subdomain = '.'.join(subdomains[sub:])
                visit[subdomain] = visit.get(subdomain, 0) + count
        res =[]
        for subdomain ,count in visit.items():
            res.append(f"{count} {subdomain}")
        return res








