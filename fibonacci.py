n = int(input())
l = [0, 1]
for i in range(n):
	if i == 0 or i == 1:
		continue
	fibo = l[i-1] + l[i-2]
	l.append(fibo)
for item in l:
	print(str(item))