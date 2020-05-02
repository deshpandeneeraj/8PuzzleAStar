"""
@Author : Neeraj Deshpande
 Date: 2 May 2020
@GitHub ID : deshpandeneeraj
 GitHub Link : https://github.com/deshpandeneeraj/8PuzzleAStar
"""


def manhattan_dis(state):
    if len(state) == 9:
        distance = 0
        for index, value in enumerate(state):
            if value == 0:
                continue
            actual = index + 1
            while not value == actual:
                #Vertical Distance
                if abs(value - actual) >= 3:
                    if value < actual:
                        actual -= 3
                        distance += 1
                    else:
                        actual += 3
                        distance += 1
                #Horizontal Distance
                elif value < actual:
                    actual -= 1
                    distance += 1
                elif value > actual:
                    actual += 1
                    distance += 1
            # print(f"Value = {value} , Distance = {distance}")
        return distance
    else:
        return False

class Node():

    def __init__(self, depth = 0, state = None):
        self.depth = depth
        self.state = state
        self.cost = manhattan_dis(state)
        self.priority = self.cost + self.depth

    def get_priority(self):
        return self.priority

    def get_state(self):
        return self.state

    # index = 0, {1, 3}
    # index = 1, {0, 2, 4};
    # index = 2, {1, 5};
    # index = 3, {4, 0, 6};
    # index = 4, {3, 5, 1, 7};
    # index = 5, {4, 2, 8};
    # index = 6, {7, 3};
    # index = 7, {6, 8, 4};
    # index = 8, {7, 5};
    #Generate possible neighbours for moves
    def generate_neighbours(self):
        neighbours = []
        index = self.state.index(0)
        if index == 0:
            neighbours = [1, 3]
        elif index == 1:
            neighbours = [0, 2, 4]
        elif index == 2:
            neighbours = [1, 5]
        elif index == 3:
            neighbours = [4, 0, 6]
        elif index == 4:
            neighbours = [3, 5, 1, 7]
        elif index == 5:
            neighbours = [4, 2, 8]
        elif index == 6:
            neighbours = [7, 3]
        elif index == 7:
            neighbours = [6, 8, 4]
        elif index == 8:
            neighbours = [7, 5]
        return neighbours

    #return new state after swapping
    def swap(self, index_target):
        index_blank = self.state.index(0)
        new_state = self.state.copy()
        if new_state[index_blank] == 0:
            i1 = new_state[index_target]
            new_state[index_target] = 0
            new_state[index_blank] = i1
            return new_state
        else:
            return False


if __name__ ==  "__main__":
    start = [1, 2, 3, 4, 5, 0, 7, 8, 6]
    target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    current_depth = 0

    parent = Node(state=start, depth=current_depth)
    neighbours = parent.generate_neighbours()
    children = []
    result = False
    while not result:
        current_depth += 1
        for i in neighbours:
            children.append(Node(state=parent.swap(i), depth=current_depth))
        print(children)
        for i in children:
            if i.get_state() == target:
                result = True
                cost = i.get_priority()
                final = i.get_state()
        min_cost = 999
        for i in children:
            if i.get_priority() < min_cost:
                state = i.get_state()
                min = i.get_priority()
        parent = Node(state = state, depth=current_depth)
        print("Current depth = ", current_depth)
        children = []
    print("Start State:")
    for i in range(0,9,3):
        print(start[i], start[i+1], start[i+2])

    print("\nTarget State:")
    for i in range(0, 9, 3):
        print(target[i], target[i + 1], target[i + 2])

    print(f"\nTotal Number of Moves : {cost}")

