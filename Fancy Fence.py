def can(angle):
    if angle < 60 or angle >= 180:
        return False
    n = 360/(180-angle)
    if n.is_integer() and n >= 3:
        return True

a=int(input())
for _ in range(a):
    angle=int(input())
    result=can(angle)
    if result:
        print("YES")
    else:
        print("NO")