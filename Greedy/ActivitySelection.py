#  Activty Selection problem using Greedy Algorithm

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]]

def activitySelection(activities: dict) -> int:

    activities.sort(key=lambda x:x[2])
    i = 0
    print(activities[i][0])
    count = 1

    for j in range(1, len(activities)):
        if activities[j][1] >= activities[i][2]:
            print(activities[j][0])
            count += 1
            i = j
        
    return count

print(activitySelection(activities))
