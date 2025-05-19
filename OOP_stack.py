class Stack:
    def __init__(self):
        self.__items = []
        self.__isEmpty = True
        self.__length = 0
    
    @property
    def peek(self):
        if len(self) > 0:
            return self.__items[-1]
        else:
            raise IndexError('Peeking an empty Stack')
    
    def push(self, item):
        self.__items.append(item)
        self.__length += 1
        self.__isEmpty = False
    
    def pop(self):
        if len(self) > 0:
            self.__items.pop(-1)
            self.__length -= 1
            if self.__length == 0:
                self.__isEmpty = True
        else:
            raise IndexError('Popping from an empty Stack')
    
    @property
    def isEmpty(self):
        return self.__isEmpty

    def __len__(self):
        return self.__length
    

new_stack = Stack()
new_stack.push(12)
print(new_stack.peek)
print(len(new_stack))
print(new_stack.isEmpty)
