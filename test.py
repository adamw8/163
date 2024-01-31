import time
import solver
import pickle
from tqdm import tqdm

def test():
    # Read in solutions from pickle file
    with open('solutions/all_test_cases.pkl', 'rb') as f:
        all_test_cases = pickle.load(f)
    solvable_test_cases = all_test_cases['solvable']
    unsolvable_test_cases = all_test_cases['unsolvable']

    # Test solvable cases
    start_time = time.time()
    for cards, _ in tqdm(solvable_test_cases.items()):
        solvable, solution = solver.solve_163(cards)
        if not solvable:
            print(f'Failed solvable test case: {cards}')
    time_for_solvable_tests = time.time() - start_time
    print(f'Avg solve time for solvable cases: {time_for_solvable_tests / len(solvable_test_cases)}')
    
    # Test unsolvable cases
    start_time = time.time()
    for cards, _ in tqdm(unsolvable_test_cases.items()):
        solvable, solution = solver.solve_163(cards)
        if solvable:
            print(f'Discovered solution to unsolvable test case: {cards}')
            print(f'Solution: {solution}')
    time_for_unsolvable_tests = time.time() - start_time
    print(f'Avg solve time for unsolvable cases: {time_for_unsolvable_tests / len(unsolvable_test_cases)}')

    print(f'Avg solve time for all cases: {(time_for_solvable_tests + time_for_unsolvable_tests) / (len(solvable_test_cases) + len(unsolvable_test_cases))}')


if __name__ == '__main__':
    test()