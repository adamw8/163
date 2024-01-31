import solver
import itertools
from tqdm import tqdm
import os
import pickle

def main():
    if os.path.exists("solutions/all_solutions.txt"):
        delete = input("Delete existing solutions file? (y/n): ")
        if delete in ['y', 'yes', 'Y', 'Yes']:
            os.remove("solutions/all_solutions.txt")
        else:
            return
        
    if not os.path.exists("solutions/all_test_cases.pkl"):
        generate_test_cases()
    
    with open('solutions/all_test_cases.pkl', 'rb') as f:
        all_test_cases = pickle.load(f)
    solvable_test_cases = all_test_cases['solvable']
    unsolvable_test_cases = all_test_cases['unsolvable']

    # get all combinations
    print("Compiling all combinations...")
    all_combinations = []
    for cards in solvable_test_cases.keys():
        all_combinations.append(cards)
    for cards in unsolvable_test_cases.keys():
        all_combinations.append(cards)
    all_combinations.sort()
        
    
    print("Writing draws to file...")
    solution_file = open("solutions/all_solutions.txt", "a")
    for cards in tqdm(all_combinations):
        if cards in solvable_test_cases:
            solution = solvable_test_cases[cards]
        else:
            solution = 'Unsolvable'
        solution_file.write(f'{cards}: {solution}\n')
    
    # collect statistics    
    total_combinations = len(all_combinations)
    total_solvable = len(solvable_test_cases)
    solvable_percentage = 100.0 * total_solvable / total_combinations
    solution_file.write(f'{total_solvable} / {total_combinations} ({solvable_percentage:.3f}%) are solvable.')
    solution_file.close()

def generate_test_cases():
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
    all_test_cases = {'solvable': {},
                      'unsolvable': {}}
    for cards in tqdm(all_combinations):
        solvable, solution = solver.solve_163(cards)
        all_test_cases['solvable' if solvable else 'unsolvable'][tuple(cards)] = solution
    
    with open('solutions/all_test_cases.pkl', 'wb') as f:
        pickle.dump(all_test_cases, f)
    
    print(len(all_test_cases['solvable']), len(all_test_cases['unsolvable']))

if __name__ == '__main__':
    main()
