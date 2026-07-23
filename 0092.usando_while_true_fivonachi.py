a = 0
b = 1
c = 0
i = 1
while True:
  if i > 10:
    break
  print(a)
  c = a + b
  a = b
  b = c
  i += 1