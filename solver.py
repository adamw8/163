from typing import List, Tuple
import math

def solve_163(cards: List[int]) -> Tuple[bool, str]:
    return solve(cards, 163)

def solve(cards, target) -> Tuple[bool, str]:
    sorted_cards = sorted(cards, reverse=False)
    solvable, solution = _solve_recursively(sorted_cards, target)
    if solvable:
        assert eval(solution) == target
        # remove end parentheses
        if solution[0] == '(' and solution[-1] == ')':
            solution = solution[1:-1] # remove end parentheses
    return solvable, solution

def _try_addition(cards: List[int], card: int, target: int) -> Tuple[bool, str]:
    return _solve_recursively(cards, target - card)

def _try_subtraction(cards: List[int], card: int, target: int) -> Tuple[bool, str]:
    return _solve_recursively(cards, target + card)

def _try_multiplication(cards: List[int], card: int, target: int) -> Tuple[bool, str]:
    if card == 0:
        return False, 'Unsolvable'
    elif target % card == 0:
        return _solve_recursively(cards, target // card)
    else:
        return False, 'Unsolvable'
    
def _try_division(cards: List[int], card: int, target: int) -> Tuple[bool, str]:
    return _solve_recursively(cards, target * card)

OPERATIONS = {
    '+': _try_addition,
    '-': _try_subtraction,
    '*': _try_multiplication,
    '/': _try_division
}

def _solve_recursively(cards: List[int], 
                       target: int) -> Tuple[bool, str]:
    # base case
    if len(cards) == 1:
        return (True, str(cards[0])) if cards[0] == target else (False, 'Unsolvable')
    
    # num_ones = 0
    # for card in cards:
    #     num_ones = num_ones + 1 if card == 1 else num_ones

    # # Prune: all ones
    # if num_ones == len(cards):
    #     if target < 0 or target > num_ones:
    #         return False, 'Unsolvable'
    #     if target == 1:
    #         return True, '*'.join(['1' for _ in range(len(cards))])
    #     else:
    #         add_str = '+'.join(['1' for _ in range(target)])
    #         add_str = f'({add_str})'
    #         mult_str = '*'.join(['1' for _ in range(num_ones-target)])
    #         return True, f'{add_str}*{mult_str}'

    # # Prune: product check
    # product_cards = [card for card in cards if card != 1]
    # if len(product_cards) > 0:
    #     # product has at least 1 card
    #     while num_ones > 0:
    #         idx = index_of_min(product_cards)
    #         product_cards[idx] = product_cards[idx] + 1
    #         num_ones -= 1

    #     product = math.prod(product_cards)
    #     if product < target:
    #         return False, 'Unsolvable'
    
    
    num_cards = len(cards)
    for i in range(num_cards):
        remanining_cards = cards[:i] + cards[i+1:]
        card = cards[i]
        
        # try all combinations of operations
        for op_str, operation in OPERATIONS.items():
            solvable, solution = operation(remanining_cards, card, target)
            if solvable:
                return True, f'({solution}{op_str}{card})'
            
    # tried all combinations    
    return False, 'Unsolvable'

def index_of_min(l: List[int]) -> int:
    min_index = 0
    for i in range(len(l)):
        if l[i] < l[min_index]:
            min_index = i
    return min_index