# https://codeforces.com/problemset/problem/1/A
def theatreSquare(m,n,a):
    if m%a == 0 and n%a ==0:
        return (m//a )*(n //a)
    if m%a > 0 and n%a ==0:
        return ((m//a)+1) * (n //a)
    if m%a ==0 and n%a >0:
        return (m//a) *((n //a)+1)
    if m%a > 0 and n%a > 0:
        return ((m//a)+1) *((n //a)+1)
