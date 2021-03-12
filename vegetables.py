s1 = 'картошка'
s2 = 'огурец'
s3 = 'помидор'
s1 = s1.upper()
s2 = s2.upper()
s3 = s3.upper()
print(s1)
print(s2)
print(s3)
s1 = s1.lower()
s2 = s2.lower()
s3 = s3.lower()
print(s1)
print(s2)
print(s3)
print(s1.title())
print(s2.title())
print(s3.title())
s1 = "картош"
a = int(input("Введите первое количество "))
if a == 1:
        s1 = s1 + "ка"
        s11 = "1 " + s1
elif a > 4:
        s1 = s1 + "ин"
        s11 = str(a) + s1
elif a > 1:
        s1 = s1 + "ки"
        s11 = str(a) + s1
else:
        print(" картошин нет ")
b = int(input("Введите второе количество "))
if b == 1:
        s12 = "1 " + s2
elif b > 4:
        s2 = s2 + "ов"
        s12 = str(b) + s2
elif b > 1:
        s2 = s2 + "а"
        s12 = str(b) + s2
else:
        print(" огурцов нет ")
c = int(input("Введите третье количество "))
if c == 1:
        s13 = "1 " + s3
elif c > 4:
        s3 = s3 + "ов"
        s13 = str(c) + s3
elif c > 1:
        s3 = s3 + "а"
        s13 = str(c) + s3
else:
        print(" помидоров нет ")
text = """Общее количество овощей :{0}, {1} и {2}.""".format(s11, s12, s13)
print(text)
input()
