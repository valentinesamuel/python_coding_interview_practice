from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')


def is_balanced(exp):
    """
    PROBLEM: In this problem, you have to implement the is_balanced() function which will take a string containing only curly {}, square [], and round () parentheses. The function will tell us whether all the parentheses in the string are balanced or not.
    For all the parentheses to be balanced, every opening parenthesis must have a closing one. The order in which they appear also matters. For example, {[]} is balanced, but {[}] is not.

    Input: A string consisting solely of (, ), {, }, [, and ]

    Output: It returns True if the expression contains balanced parentheses and returns False otherwise.

    Example Input: 
    exp = "{[({})]}"

    Example Output:
    True

    APPROACH:
    - Initial thoughts: Add every opening sign, if the sign at the top of the stack is not the corresponding sign of the current sign, then there is no match

    - Plan: 
        - create an array of closing signs
        - for every character in the string, if the current sign is in the closing array of signs: 
            - if the stack is empty, thn there is no sign to comapre with, so we return fals
            - we pop the stack
            - and if the current sign does not correspond with the popped sign, we return False
        - if the current sign is not in the array of closing sign then it is an opening sign, so we just ass the sign to the stack
        - if the stack is not empty after all comparisons, then the number of signs are not balanced, so we return False
        - is we were not able to return False since, then we return True.
    """
    closing = ['}', ')', ']']
    stack = Stack()
    for character in exp:
        if character in closing:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if character == '}' and top_element != '{':
                return False
            if character == ')' and top_element != '(':
                return False
            if character == ']' and top_element != '[':
                return False
        else:
            stack.push(character)
    if not stack.is_empty():
        return False
    return True
