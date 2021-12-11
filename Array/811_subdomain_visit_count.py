from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split(".")
            for i in range(len(frags)):
                hashmap[".".join(frags[i:])] += count

        return ["{} {}".format(c, d) for d, c in hashmap.items()]


class Solution:
    def split_domain(self, s):
        s = s.split(" ")
        num = s[0]
        s = s[1].split(".")
        res = [int(num)]
        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                sub += "." + s[j]
            res.append(sub.strip("."))
        return res

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        for s in cpdomains:
            output = self.split_domain(s)
            for subdomain in output[1:]:
                hashmap[subdomain] += output[0]
        res = []
        for key, val in hashmap.items():
            res.append(str(val) + " " + key)

        return res
