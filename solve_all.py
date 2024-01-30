import solver
import itertools
import time
from tqdm import tqdm
from typing import List
import os
import math

def main():  
    if os.path.exists("all_solutions.txt"):
        delete = input("Delete exists solutions file? (y/n): ")
        if delete in ['y', 'yes', 'Y', 'Yes']:
            os.remove("all_solutions.txt")
        else:
            return
    
    # create deck of cards
    start_time = time.time()
    all_cards = []
    for i in range(1, 14):
        for _ in range(4):
            all_cards.append(i)
    deck_size = len(all_cards)

    # write all solutions to file
    solution_file = open("all_solutions.txt", "a")
    total_combinations = 0
    total_solvable = 0
    for indices in tqdm(itertools.combinations(range(deck_size), 6), total=math.comb(deck_size, 6)):
        cards = [all_cards[i] for i in indices]
        solvable, solution = solver.solve_163(cards)
        solution_file.write(f'{cards}: {solution}\n')

        if solvable:
            total_solvable += 1
        total_combinations += 1
    
    # collect statistics
    end_time = time.time()
    solvable_percentage = 100.0 * total_solvable / total_combinations
    solution_file.write(f'\nSolve all combinations in {end_time - start_time:.3f} seconds.\n')
    solution_file.write(f'{total_solvable} / {total_combinations} ({solvable_percentage:.3f}%) are solvable.')
    solution_file.close()

if __name__ == '__main__':
    main()
