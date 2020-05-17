class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction, x , y ,distance= 0,0,0,0
        obstacles_dict = {}

        for obs in obstacles:
            obstacles_dict[tuple(obs)] = 1

        for cmd in commands:
            if cmd == -2:
                direction = (direction+3)%4
            elif cmd == -1:
                direction = (direction+1)%4
            else:
                dx,dy = directions[direction]
                for i in range(cmd):
                    next_x = x +dx
                    next_y = y +dy
                    if (next_x,next_y) in obstacles_dict:
                        break
                    x,y = next_x,next_y
                    distance = max(distance, x**2+y**2)

        return distance