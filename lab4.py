import time
import random
import itertools


def is_even(combo):
    rank1 = combo[0][0]
    rank2 = combo[1][0]
    return (ranks_numbers[rank1] + ranks_numbers[rank2]) % 2 == 0


while True:
    task = int(input("Enter task(6 or 8): "))
    if task == 6:
        # task 6
        def retry(attempts, delay):
            def decorator(func):
                def wrapper(*args, **kwargs):
                    for _ in range(attempts):
                        try:
                            return func(*args, **kwargs)
                        except Exception as e:
                            print(f"An error occurred: {e}. Retrying...")
                            time.sleep(delay)
                return wrapper
            return decorator

        @retry(attempts=3, delay=0.5)
        def fetch_data_from_flaky_service():
            if random.random() < 0.7:
                raise ConnectionError("Service is unavailable")
            return {"data": "some value"}

        fetch_data_from_flaky_service()


    elif task == 8:
        # task 8
        ranks = ['10', 'J', 'Q', 'K', 'A']
        ranks_numbers = {
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        deck = list(itertools.product(ranks, suits))
        combos_iterator = itertools.combinations(deck, 2)

        even_combos = list(filter(is_even, combos_iterator))

        print(f"Total even combinations: {len(even_combos)}")
        for even_combo in even_combos:
            print(even_combo)

    elif task == 0:
        print("Exiting the program...")
        exit()
