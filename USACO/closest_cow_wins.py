kmn = input().split()
k = int(kmn[0])
m = int(kmn[1])
n = int(kmn[2])

kpos = []
sorted_k_pos = []
ksweetness = []
for i in range(k):
    kandsweetness = input().split()
    kpos.append(int(kandsweetness[0]))
    sorted_k_pos.append(int(kandsweetness[0]))
    ksweetness.append(int(kandsweetness[1]))

cow_pos = []
sorted_cow_pos = []
for i in range(m):
    cow_pos.append(int(input()))
    sorted_cow_pos.append(int(input()))

closest_dist = []
for i in kpos:
    for a in cow_pos:
        if i == 0:
            if i > a:
                temporary_closest_dist = i-a
            else:
                temporary_closest_dist = a-i
        else:
            if i > a:
                if i - a < temporary_closest_dist:
                    temporary_closest_dist = i-a
            else:
                if a - i < temporary_closest_dist:
                    temporary_closest_dist = a-i
    closest_dist.append(temporary_closest_dist)

furthest_pos = 0
sorted_k_pos.sort(reverse=True)
cow_pos.sort(reverse=True)
if sorted_k_pos[0] > sorted_cow_pos[0]:
    furthest_pos = sorted_k_pos[0]
else:
    furthest_pos = sorted_cow_pos[0]

value = []
for i in range(furthest_pos):
    for a in range(len(kpos)):
        if kpos[a] > i:
