# List as stacks
# The last element in the list, is the first to be removed in the stack
stack = [3, 4, 5]
# Add a last item to the stack/list
stack.append(7)
# Pop out the last item
# stack.pop()
# print(stack.pop())

# List as queues
from collections import deque
arrival = deque(["Denzel", "Murathi", "Gitonga"]) # The initial arrival list
arrival.append("Cate") # Cate arrives last
# To pop from the beginning, as first in, first out, quickly
# print(arrival.popleft())

# List comprehension
# squares = []
# for x in range(10):
#     squares.append(x**2)
# VS
squares = [x**2 for x in range(10)]
# print(squares)
# For conditions
# combo = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combo.append((x,y))

# VS
combo = [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(combo)
squares_2 = [(x, x**2) for x in range(6)]
for x, y in squares_2:
    print("The square of {} is {}".format(x, y))