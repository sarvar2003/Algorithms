def sortFabrics(fabrics):

    count = 0

    Ada = sorted(fabrics, key=lambda x:(x[0], x[2]))
    Charles = sorted(fabrics, key=lambda x:(x[1], x[2]))
    

    for i in range(len(fabrics)):

        if Ada[i] == Charles[i]:
            count += 1

    return count


def main():
  T = int(input())
  for test_case in range(1, T + 1):
    N = int(input())
    fabrics = []

    for _ in range(N):
        c,d,i = input().split()
        fabrics.append([c, int(d), int(i)])

    ans = sortFabrics(fabrics)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()