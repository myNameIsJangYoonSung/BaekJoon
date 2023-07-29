point = [list(map(int, input().split())) for _ in range(3)]

xpoint = []
ypoint = []
resultx = 0
resulty = 0
for i in range(3):
  xpoint.append(point[i][0])
  ypoint.append(point[i][1])

maxx = max(xpoint)
minx = min(xpoint)
maxy = max(ypoint)
miny = min(ypoint)
if xpoint.count(maxx) == 1:
  resultx = maxx
else:
  resultx = minx

if ypoint.count(maxy) == 1:
  resulty = maxy
else:
  resulty = miny
print(resultx, resulty)
  