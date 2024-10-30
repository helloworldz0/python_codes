import math

# Input data
h = []
v = []
t = 0
# acceleration due to gravity
g = 9.81
# height of the gun
height = 50

for i in range(300,-1,-20):
    h.append(i)

for i in range (0,301,20):
    v.append(i)

# print(h)
# print(v)

for i in range(0,16):
    uh = h[i]
    uv = v[i]
    # print(uh)
    # print(uv)
    