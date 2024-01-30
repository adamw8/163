import random
import time
import solver


def test():
    num_solved = 0
    avg_solve_time = 0.0
    total_solves = 10000
    # TODO: read all combinations from a yaml file to evalute on all combos
    # TODO: Label each combination with a solvable or unsolvable
    # TODO: compute solve times for solvable and unsolvable separately as well
    while num_solved < total_solves:
        start_time = time.time()
        cards = [random.randint(1, 13) for _ in range(6)]
        solvable, solution = solver.solve_163(cards)
        end_time = time.time()
        print(solution)
        if solvable:
            avg_solve_time += (end_time - start_time) / total_solves
            num_solved += 1
    print(f'Average solve time: {avg_solve_time}')

def main():
    cards, target = get_user_input()
    if target == 163:
        solvable, solution = solver.solve_163(cards)
    else:
        solvable, solution = solver.solve(cards, target)
    
    # unsolvable
    if not solvable:
        print("Unsolvable.")
        return
    
    # solvable
    view_solution = input('Solvable! View solution (y/n)? ')
    if view_solution in ['y', 'yes', 'Y', 'Yes']:
        print(solution)
    else:
        print('Goodluck, keep trying ;)')

def get_user_input():
    input_cards = input("Enter cards as csv (1 for A, 11 for J, 12 for Q, 13 for K): ")
    input_cards = input_cards.split(',')
    cards = [int(card) for card in input_cards]

    # Get target number from user
    target = input("Enter target number (if 163, press Enter): ")
    if target == '':
        target = 163
    
    return cards, target


if __name__ == '__main__':
    # test()
    main()