from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')


def evaluate_post_fix(exp: str):
    """
    PROBLEM: The usual convention followed in mathematics is the infix expression. Operators like + and * appear between the two numbers involved in the calculation:

    6 + 3 * 8 - 4
    Another convention is the postfix expression where the operators appear after the two numbers involved in the expression. In postfix, the expression written above will be presented as:

    6 3 8 * + 4 -
    The two digits preceding an operator will be used with that operator

    1. From the first block of digits 6 3 8, we pick the last two which are 3 and 8.
    2. Reading the operators from left to right, the first one is *. The expression now becomes 3 * 8
    3. The next number is 6 while the next operator is +, so we have 6 + 8 * 3.
    4. The value of this expression is followed by 4, which is right before -. Hence we have 6 + 8 * 3 - 4.
    Implement a function called evaluatePostFix() that will compute a postfix expression given to it as a string.


    Input: A string containing a postfix mathematic expression. Each digit is considered to be a separate number, i.e., there are no double digit numbers.

    Output: A result of the given postfix expression.

    Example Input: 
    exp = "921 * - 8 - 4 +" # 9 - 2 * 1 - 8 + 4

    Example Output:
    3

    APPROACH:
    - Initial thoughts: I tried but i could not solve it before my trial time of 30 mins elapsed

    - Plan: 
        - loop through the elements in the expression
        - if the current element is a number, push it onto the stack
        - if not, pop the left and right element respectively
        - push the stringified evaluated result of right + element + left onto the stack
        - finally, return the floated, integerised version of the number that is popped off the stack
        - Because we are adding the the result of very operation that we do, we are able to retain BODMAS operations.
    """
    stack = Stack
    for ele in exp:
        if ele.isdigit():
            stack.push(ele)
        else:
            left = stack.pop()
            right = stack.pop()
            stack.push(str(eval(right + ele + left)))
    return int(float(stack.pop()))
