# from collections import Counter

a=["MIT","ACLU","UCB","UCLA"]

b=["MIT","Apache","Mozilla","GNU general public","gnu public general public", "gnu affero general public LICENSE","BSD-3-Clause"]

# print(Counter(a)==Counter(b))

s=set(a).intersection(b)
m="".join(s)
print(m)
