# Source: https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

# Define Infinite (Using INT_MAX 
# caused overflow problems)
INT_MAX = 10000


# Given three colinear points p, q, r,
# the function checks if point q lies
# on line segment 'pr'
def onSegment(p: tuple, q: tuple, r: tuple) -> bool:
    if ((q[0] <= max(p[0], r[0])) &
            (q[0] >= min(p[0], r[0])) &
            (q[1] <= max(p[1], r[1])) &
            (q[1] >= min(p[1], r[1]))):
        return True

    return False


# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are colinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p: tuple, q: tuple, r: tuple) -> int:
    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))

    if val == 0:
        return 0
    if val > 0:
        return 1  # Collinear
    else:
        return 2  # Clock or counterclock


def doIntersect(p1, q1, p2, q2):
    # Find the four orientations needed for
    # general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2) and (o3 != o4):
        return True

    # Special Cases
    # p1, q1 and p2 are colinear and
    # p2 lies on segment p1q1
    if (o1 == 0) and (onSegment(p1, p2, q1)):
        return True

    # p1, q1 and p2 are colinear and
    # q2 lies on segment p1q1
    if (o2 == 0) and (onSegment(p1, q2, q1)):
        return True

    # p2, q2 and p1 are colinear and
    # p1 lies on segment p2q2
    if (o3 == 0) and (onSegment(p2, p1, q2)):
        return True

    # p2, q2 and q1 are colinear and
    # q1 lies on segment p2q2
    if (o4 == 0) and (onSegment(p2, q1, q2)):
        return True

    return False


# Returns true if the point p lies
# inside the polygon[] with n vertices
def isInsidePolygon(points: list, p: tuple) -> bool:
    n = len(points)

    # There must be at least 3 vertices
    # in polygon
    if n < 3:
        return False

    # Create a point for line segment
    # from p to infinite
    extreme = (INT_MAX, p[1])
    count = i = 0

    while True:
        next = (i + 1) % n

        # Check if the line segment from 'p' to 
        # 'extreme' intersects with the line 
        # segment from 'polygon[i]' to 'polygon[next]'
        if (doIntersect(points[i],
                        points[next],
                        p, extreme)):

            # If the point 'p' is colinear with line 
            # segment 'i-next', then check if it lies 
            # on segment. If it lies, return true, otherwise false
            if orientation(points[i], p,
                           points[next]) == 0:
                return onSegment(points[i], p,
                                 points[next])

            count += 1

        i = next

        if (i == 0):
            break

    # Return true if count is odd, false otherwise
    return (count % 2 == 1)

def correctPointsOrder(points):
    # From: https://stackoverflow.com/questions/7009548/determining-ordering-of-vertices-to-form-a-quadrilateral
    # input: array of 4 points [(x,y),...]
    # The array is passed by reference
    # output: void
    pointsX = []
    pointsY = []
    B = findB(points)
    for i in range(4):
        pointsX.append(points[i][0] - B[0]>0)
        pointsY.append(points[i][1] - B[1]>0)

    if pointsX[0] != pointsX[1] and pointsX[0] != pointsX[1]:
        pointsX[1], pointsY[1], pointsX[2], pointsY[2] = pointsX[2], pointsY[2], pointsX[1], pointsY[1]
        points[1], points[2] = points[2], points[1]
    if pointsX[2] != pointsX[1] and pointsX[2] != pointsX[1]:
        pointsX[3], pointsY[3], pointsX[2], pointsY[2] = pointsX[2], pointsY[2], pointsX[3], pointsY[3]
        points[3], points[2] = points[2], points[3]


def findB(points):
    x = (points[0][0] + points[1][0] + points[2][0] + points[3][0]) / 4
    y = (points[0][1] + points[1][1] + points[2][1] + points[3][1]) / 4
    return x, y


# Driver code
if __name__ == '__main__':
    # order of points
    pointss = []
    pointss.append([6, 6])
    pointss.append([3, 8])
    pointss.append([5, 3])
    pointss.append([2, 4])

    # print(line_intersection((points[0], points[1]), (points[2], points[3])))
    print(correctPointsOrder(pointss))
    print(pointss)

    # isInsidePolygon():
    polygon1 = [(40.23303537721135, 29.00271397264268), (40.23066004757029, 29.002756887986664), (40.23054537437684,29.008700663151018),(40.23308452108256,29.008636290134973)]

    p = (40.23341214597919, 29.006329590384837)
    if isInsidePolygon(points=polygon1, p=p):
        print('Yes')
    else:
        print('No')

    p = (40.231970584570526, 29.002091700154665)
    if (isInsidePolygon(points=polygon1, p=p)):
        print('Yes')
    else:
        print('No')


    p = (40.23196239379306, 29.00536399514479)
    if (isInsidePolygon(points=polygon1, p=p)):
        print('Yes')
    else:
        print('No')

    p = (40.23150370867489, 29.00668364198293)
    if isInsidePolygon(points=polygon1, p=p):
        print('Yes')
    else:
        print('No')

    p = (-1, 10)
    if isInsidePolygon(points=polygon1, p=p):
        print('Yes')
    else:
        print('No')

# This code is contributed by Vikas Chitturi