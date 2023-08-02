import math
def dist(x1 , x2):
    return math.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

def find_closest_dist(X):
    n = len(X)
    if n == 2:
        return dist(X[0] , X[1])
    elif n == 3:
        return min(dist(X[0] , X[1]) , dist(X[1] , X[2]) , dist(X[2] , X[0]))
    
    X.sort()
    x_mid = X[n//2]
    left = find_closest_dist(X[:n//2])
    right = find_closest_dist(X[n//2:])

    min_dist = min(left , right)
    
    in_between = []
    for i in range(n):
        if abs(X[i][0] - x_mid[0]) < min_dist:    
            in_between.append(X[i])

    return min(min_dist , find_closest_y(in_between , min_dist))

def find_closest_y(y , d):
    y.sort(key = lambda y:y[1])
    n = len(y)

    min_dist = d
    for i in range(n):
        for j in range(i+1 , n):
            if abs(y[i][1] - y[j][1]) >= d:
                break

            distance = dist(y[i], y[j])
            if distance < min_dist:
                min_dist = distance
    
    return min_dist

if __name__ == "__main__":
    case = int(input())
    output = []
    for i in range(case):
        case_num = int(input())
        points = []
        for n in range(case_num):
            point = input()
            point = point.split(' ')
            points.append([float(i) for i in point])
        print(find_closest_dist(points))
