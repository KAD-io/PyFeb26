def test02_task07(s='abcdefghijklmnopqrstuvwxyz', n=4):
    s1 = s[0:n]
    s2 = s[0:n - 1]
    print(s1+s2[::-1])


test02_task07()