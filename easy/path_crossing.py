class Solution(object):
    def isPathCrossing(self, path):
        point_x = 0
        point_y = 0

        visited = {(0,0)}

        for char in path:
            if char == "N":
                point_y += 1
            elif char == "S":
                point_y -= 1
            elif char == "W":
                point_x -= 1
            elif char == "E":
                point_x += 1

            current = (point_x, point_y)

            if current in visited:
                return True
            
            visited.add(current)

        return False