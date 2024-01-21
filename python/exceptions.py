for i in range(int(input())):
    case = input().split()
    try:
        res = int(case[0])//int(case[1])
    except Exception as e:
        print("Error Code:", e)
    else:
        print(res)
