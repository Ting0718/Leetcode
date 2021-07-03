# "string".index(element, start, end)
s = "kitty"
print(s.index("t"))
print(s.index("t", 2))  # search for the second one
# gives errors if cannot find the substring


# enumerate: useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
l = ["hello", "goodbye", "hey", "goodmorning"]
for index, s in enumerate(l):
    print(index, s)

    # 0 hello
    # 1 goodbye
    # 2 hey
    # 3 goodmorning


# whenever pop is called, the last element is out, stack.pop() -> [1,2,3,4]
stack = [1, 2, 3, 4, 5]
stack.pop()  # stack
# pop remove the last one
# the stack cannot be empty. check length beforehand


queue = [1, 2, 3, 4, 5]
queue.pop(0)  # queue


# .find(substring) returns the index of the substring
# string.find(value, start, end)
s = "hello"
sub = "ll"
s.find(sub)
# return -1 if not found
