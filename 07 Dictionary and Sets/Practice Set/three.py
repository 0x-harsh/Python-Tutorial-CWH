s = set()

s.add(18)
s.add("18")

print(s)

s1 = set()
s1.add(20)
s1.add(20.0)
s1.add('20')
print(s1, len(s1))