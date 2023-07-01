st=input()
st1=list(st)
vowels="aeiou"
for i in st1:
    if i in vowels:
        st1.remove(i)
print("".join(st1))
