import random
import time
import solver


def test():
    num_solved = 0
    avg_solve_time = 0.0
    total_solves = 100
    while num_solved < total_solves:
        start_time = time.time()
        cards = [random.randint(1, 13) for _ in range(6)]
        solvable, solution = solver.solve_163(cards)
        end_time = time.time()
        avg_solve_time += (end_time - start_time) / total_solves
        num_solved += 1
    print(f'Average solve time: {avg_solve_time}')


if __name__ == '__main__':
    test()