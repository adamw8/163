import copy
from typing import List, Tuple, Callable

def solve_163(cards: List[int]) -> Tuple[bool, str]:
    # simple heuristic to speed up solves
    sorted_cards = sorted(cards, reverse=False)
    return solve(sorted_cards, 163)

def solve(cards, target) -> Tuple[bool, str]:
    solvable, solution = _solve_recursively(cards, target)
    if solvable:
        assert eval(solution) == target
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
        return _solve_recursively(cards, target / card)
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
    if len(cards) == 1 and cards[0] == target:
        return True, str(cards[0])
    
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