class Group:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sameGroupTest(self, rules):
        mistakes = 0
        if self.a in rules:
            for name in reversed(rules[self.a]):
                if name != self.b and name != self.c:
                    mistakes += 1
                    rules[self.a].remove(name)
        if self.b in rules:
            for name in reversed(rules[self.b]):
                if name != self.a and name != self.c:
                    mistakes += 1
                    rules[self.b].remove(name)
        if self.c in rules:
            for name in reversed(rules[self.c]):
                if name != self.b and name != self.a:
                    mistakes += 1
                    rules[self.c].remove(name)
        return mistakes, rules

    def diffGroupTest(self, rules):
        mistakes = 0
        if self.a in rules:
            for name in reversed(rules[self.a]):
                if name == self.b or name == self.c:
                    mistakes += 1
                    rules[self.a].remove(name)
        if self.b in rules:
            for name in reversed(rules[self.b]):
                if name == self.a or name == self.c:
                    mistakes += 1
                    rules[self.b].remove(name)
        if self.c in rules:
            for name in reversed(rules[self.c]):
                if name == self.b or name == self.a:
                    mistakes += 1
                    rules[self.c].remove(name)
        return mistakes, rules

sameGroups = {}
diffGroups = {}
mistakes = 0

x = int(input())
for i in range(x):
    rule = input().split(' ')
    if rule[0] not in sameGroups:
        sameGroups[rule[0]] = [rule[1]]
    else:
        sameGroups[rule[0]].append(rule[1])
y = int(input())
for i in range(y):
    rule = input().split(' ')
    if rule[0] not in diffGroups:
        diffGroups[rule[0]] = [rule[1]]
    else:
        diffGroups[rule[0]].append(rule[1])
g = int(input())
for i in range(g):
    group = Group(*input().split(' '))
    n, sameGroups = group.sameGroupTest(sameGroups)
    mistakes += n
    n, diffGroups = group.diffGroupTest(diffGroups)
    mistakes += n

print(mistakes)