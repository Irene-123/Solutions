file=open('/home/kirti/Downloads/input.txt','r')
contents=file.read()
seats=list(contents.split('\n'))[:-1]


def binsearch(lo, hi, pattern):
    # pattern is a list of booleans, where each is True if in the lower half
    # and False otherwise.
    for c in pattern:
        mid = lo + (hi - lo)//2
        if c:
            hi = mid
        else:
            lo = mid
    return lo

seat_ids=[]
d={}
for s in seats:
    row_pattern = [c == 'F' for c in s[:7]]
    col_pattern = [c == 'L' for c in s[7:]]
    row = binsearch(0, 127, row_pattern) + 1
    col = binsearch(0, 7, col_pattern) + 1
    id_=row * 8 + col
    d[id_] = (row, col)
    #print(s, 'row:', row, 'col:', col)
    seat_ids.append(row * 8 + col)

#print(sorted(seat_ids))
#print('\n'.join('{}: {}'.format(a, d[a]) for a in sorted(d)))

your_seat = [s for s in range(min(seat_ids), max(seat_ids))
            if s not in seat_ids][0]
print(your_seat)            
