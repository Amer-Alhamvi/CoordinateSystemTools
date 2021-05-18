class CoordinateSystemTools:
    # Source: https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

    # Define Infinite (Using INT_MAX
    # caused overflow problems)
    INT_MAX = 10000
    points = []

    def __init__(self, p1, p2, p3, p4):
        self.points = [p1, p2, p3, p4]
        self.correctPointsOrder()

    # Given three colinear points p, q, r,
    # the function checks if point q lies
    # on line segment 'pr'
    def onSegment(self, p: tuple, q: tuple, r: tuple) -> bool:
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
    def orientation(self, p: tuple, q: tuple, r: tuple) -> int:
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

    def doIntersect(self, p1, q1, p2, q2):
        # Find the four orientations needed for
        # general and special cases
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # General case
        if (o1 != o2) and (o3 != o4):
            return True

        # Special Cases
        # p1, q1 and p2 are colinear and
        # p2 lies on segment p1q1
        if (o1 == 0) and (CoordinateSystemTools.onSegment(p1, p2, q1)):
            return True

        # p1, q1 and p2 are colinear and
        # q2 lies on segment p1q1
        if (o2 == 0) and (CoordinateSystemTools.onSegment(p1, q2, q1)):
            return True

        # p2, q2 and p1 are colinear and
        # p1 lies on segment p2q2
        if (o3 == 0) and (CoordinateSystemTools.onSegment(p2, p1, q2)):
            return True

        # p2, q2 and q1 are colinear and
        # q1 lies on segment p2q2
        if (o4 == 0) and (CoordinateSystemTools.onSegment(p2, q1, q2)):
            return True

        return False

    # Returns true if the point p lies
    # inside the polygon[] with n vertices
    def isInsidePolygon(self, p: tuple) -> bool:
        n = len(self.points)

        # There must be at least 3 vertices
        # in polygon
        if n < 3:
            return False

        # Create a point for line segment
        # from p to infinite
        extreme = (self.INT_MAX, p[1])
        count = i = 0

        while True:
            next = (i + 1) % n

            # Check if the line segment from 'p' to
            # 'extreme' intersects with the line
            # segment from 'polygon[i]' to 'polygon[next]'
            if (self.doIntersect(self.points[i],
                                 self.points[next],
                                 p, extreme)):

                # If the point 'p' is colinear with line
                # segment 'i-next', then check if it lies
                # on segment. If it lies, return true, otherwise false
                if self.orientation(self.points[i], p,
                                    self.points[next]) == 0:
                    return self.onSegment(self.points[i], p,
                                          self.points[next])

                count += 1

            i = next

            if (i == 0):
                break

        # Return true if count is odd, false otherwise
        return (count % 2 == 1)

    def correctPointsOrder(self):
        # From: https://stackoverflow.com/questions/7009548/determining-ordering-of-vertices-to-form-a-quadrilateral
        # input: array of 4 points [(x,y),...]
        # The array is passed by reference
        # output: void
        pointsX = []
        pointsY = []
        B = self.findB()
        for i in range(4):
            pointsX.append(self.points[i][0] - B[0] > 0)
            pointsY.append(self.points[i][1] - B[1] > 0)

        if pointsX[0] != pointsX[1] and pointsY[0] != pointsY[1]:
            pointsX[1], pointsY[1], pointsX[2], pointsY[2] = pointsX[2], pointsY[2], pointsX[1], pointsY[1]
            self.points[1], self.points[2] = self.points[2], self.points[1]
        if pointsX[2] != pointsX[1] and pointsY[2] != pointsY[1]:
            pointsX[3], pointsY[3], pointsX[2], pointsY[2] = pointsX[2], pointsY[2], pointsX[3], pointsY[3]
            self.points[3], self.points[2] = self.points[2], self.points[3]

    def findB(self):
        x = (self.points[0][0] + self.points[1][0] + self.points[2][0] + self.points[3][0]) / 4
        y = (self.points[0][1] + self.points[1][1] + self.points[2][1] + self.points[3][1]) / 4
        return x, y

    def __call__(self, point):
        return self.isInsidePolygon(point)


# Driver code
if __name__ == '__main__':
    # order of points does not matter

    polygon1 = [(40.23303537721135, 29.00271397264268), (40.23066004757029, 29.002756887986664),
                (40.23054537437684, 29.008700663151018), (40.23308452108256, 29.008636290134973)]

    a = polygon1[0]
    b = polygon1[1]
    c = polygon1[2]
    d = polygon1[3]
    # b = (3, 8)
    # c = (5, 3)
    # d = (2, 4)

    test = CoordinateSystemTools(a, b, c, d)

    # print(line_intersection((points[0], points[1]), (points[2], points[3])))
    print(test.points)

    # isInsidePolygon():

    p = (40.23341214597919, 29.006329590384837)
    print(test(p))

    p = (40.231970584570526, 29.002091700154665)
    print(test(p))

    p = (40.23196239379306, 29.00536399514479)
    print(test(p))

    p = (40.23150370867489, 29.00668364198293)
    print(test(p))

'''
    if isInsidePolygon(points=polygon1, p=p):
        print('Yes')
    else:
        print('No')

    if (isInsidePolygon(points=polygon1, p=p)):
        print('Yes')
    else:
        print('No')

    if (isInsidePolygon(points=polygon1, p=p)):
        print('Yes')
    else:
        print('No')

    if isInsidePolygon(points=polygon1, p=p):
        print('Yes')
    else:
        print('No')

    p = (-1, 10)
    if isInsidePolygon(points=polygon1, p=p):
        print('Yes')
    else:
        print('No')'''

# This code is contributed by Vikas Chitturi
