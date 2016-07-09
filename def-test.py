#!/usr/local/bin/env python3
def Intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
s1 = "Cisco123456"
s2 = "SMBCisco1256"

print(Intersect(s1, s2))
