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
print(arrival.popleft())