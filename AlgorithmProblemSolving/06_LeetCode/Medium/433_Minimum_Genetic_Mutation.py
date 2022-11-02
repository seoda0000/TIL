'''
433. Minimum Genetic Mutation
https://leetcode.com/problems/minimum-genetic-mutation/description/

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end.
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

'''
class Solution:

    def minMutation(start, end, bank):
        global ans
        ans = 9
        bank_length = len(bank)
        visited = [0] * bank_length

        def cntword(s, e):
            cnt = 0
            for i in range(8):
                if s[i] != e[i]:
                    cnt += 1
            return cnt

        def Mutation(s, cnt):
            global ans
            if cnt > ans:
                return
            if s == end:
                if cnt < ans:
                    ans = cnt
                return
            for b in range(bank_length):
                if cntword(s, bank[b]) == 1 and visited[b] == 0:
                    visited[b] = 1
                    Mutation(bank[b], cnt + 1)
                    visited[b] = 0

        Mutation(start, 0)
        if ans == 9:
            return -1
        return ans


print(Solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(Solution.minMutation("AACCGGTT","AACCGGTA", ["AACCGGTA"]))
print(Solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))

