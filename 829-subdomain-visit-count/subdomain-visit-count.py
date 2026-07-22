# for each domain, split into subdomains & bucket
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def parse_domain(domain):
            s = domain.split()
            count = int(s[0])
            domains = s[1].split('.')

            res = [''] * len(domains)
            for i in range(len(domains)):
                res[i] = '.'.join(domains[i:])

            return count, res
        
        domain_count = collections.defaultdict(int) # domain -> count

        for domain in cpdomains:
            count, domains = parse_domain(domain)
            for d in domains:
                domain_count[d] += count
    
        res = []
        for domain, count in domain_count.items():
            res.append(str(count) + ' ' + domain)

        return res