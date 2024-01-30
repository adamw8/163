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

    # Get all unique draws (suits don't matter)
    # There are much better ways of doing this, but this will work for now
    print("Generating unique draws...")
    all_indices = list(itertools.combinations(range(deck_size), 6))
    all_combinations_set = set()
    all_combinations = []
    for indices in tqdm(all_indices):
        cards = [all_cards[i] for i in indices]
        cards.sort()
        if tuple(cards) in all_combinations_set:
            continue
        else:
            all_combinations_set.add(tuple(cards))
            all_combinations.append(cards)
    del all_indices
    del all_combinations_set

    # write all solutions to file
    print("Solving all draws...")
    solution_file = open("all_solutions.txt", "a")
    total_combinations = 0
    total_solvable = 0
    for cards in tqdm(all_combinations):
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
