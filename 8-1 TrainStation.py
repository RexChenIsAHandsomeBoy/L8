datas=0
while 1>0:
    N=int(input())
    if N==0:
        break
    else:
        if datas!=0:
            print("")
        datas=datas+1
        while 1>0:
            station=[]
            B=[]
            goal=[int(x) for x in input().split()]
            if goal[0]==0:
                break
            else:
                for i in range(N):
                    station.insert(0,i+1)
                    while len(station)>0:
                        if station[0]==goal[len(B)]:
                            B.append(station[0])
                            del station[0]
                        else:
                            break
                if len(station)==0:
                    print("Yes")
                else:
                    print("No")
