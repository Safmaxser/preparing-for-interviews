class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return 'Стек пуст!'
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return 'Стек пуст!'
        return self.stack[self.size()-1]


def balanced_sequences_brackets(brackets: str) -> bool:
    possible_brackets = [['[', ']'], ['(', ')'], ['{', '}']]
    stack_brackets = Stack()
    for bracket in brackets:
        for found_brackets in possible_brackets:
            if found_brackets[0] == bracket:
                stack_brackets.push(found_brackets[1])
                break
            elif found_brackets[1] == bracket:
                if stack_brackets.pop() == bracket:
                    break
                else:
                    return False
    return True


if __name__ == '__main__':
    str_test = '(((([{}]))))'
    print(balanced_sequences_brackets(str_test))
    str_test = '[([])((([[[]]])))]{()}'
    print(balanced_sequences_brackets(str_test))
    str_test = '{{[()]}}'
    print(balanced_sequences_brackets(str_test))
    str_test = '}{}'
    print(balanced_sequences_brackets(str_test))
    str_test = '{{[(])]}}'
    print(balanced_sequences_brackets(str_test))
    str_test = '[[{())}]'
    print(balanced_sequences_brackets(str_test))
    print()

    stack = Stack()
    print(stack.peek())
    stack.push('-A-')
    stack.push('-B-')
    stack.push('-C-')
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
