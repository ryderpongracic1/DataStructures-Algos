class UnionFind:
    def __init__(self):
        self.parent = {} # email -> parent email
        self.rank = {} # email -> size of component

    def add(self, email):
        if email not in self.parent:
            self.parent[email] = email
            self.rank[email] = 1

    def find(self, email):
        if self.parent[email] != email:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self, email1, email2):
        root1, root2 = self.find(email1), self.find(email2)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for a in accounts:
            name, first_email = a[0], a[1]
            email_to_name[first_email] = name
            uf.add(first_email)

            for i in range(2, len(a)):
                next_email = a[i]
                email_to_name[next_email] = name
                uf.add(next_email)
                uf.union(first_email, next_email)

        root_to_emails = collections.defaultdict(list)

        for email in email_to_name.keys():
            root = uf.find(email)
            root_to_emails[root].append(email)

        res = []
        for root, emails in root_to_emails.items():
            emails.sort()
            name = email_to_name[root]
            res.append([name] + emails)
        return res