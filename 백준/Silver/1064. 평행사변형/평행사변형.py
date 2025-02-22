x1, y1, x2, y2, x3, y3 = map(int, input().split())

if ((y2 - y1)*(x3 - x1) == (y3 - y1)*(x2 - x1)):
    print(-1)

else:
    e1 = ((x2 - x1)**2 +(y2 - y1)**2)**(1/2)
    e2 = ((x3 - x2)**2 +(y3 - y2)**2)**(1/2)
    e3 = ((x3 - x1)**2 +(y3 - y1)**2)**(1/2)

    d = [2 * (e1 + e2), 2 * (e2 + e3), 2 * (e3 + e1)]

    print(max(d) - min(d))
