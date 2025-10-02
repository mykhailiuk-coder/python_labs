#Додай валідацію вхідних даних
from operator import indexOf
from random import choice
from collections import OrderedDict

def find_min_index(row):
    min_index = 0
    for i in range(1, len(row)):
        if row[i] < row[min_index]:
            min_index = i
    return min_index


while True:
    task = input("Input task: ")
    try:
        task = int(task)   
    except ValueError:
        print("Error: task is not an integer")
        break  

    if task == 1:
        n = input("Input n: ")
        try:
            n = int(n)
        except ValueError:
            print("Error: n is not an integer")
            break
        n = int(n)
        if n <= 0 or n > 15:
            print("Error: n is out of range [1, 15]")
            break

        A = [[0]*n for i in range(n)]

        print("Input elements: ")
        for i in range(n):
            row = list(map(float, input().split()))
            A.append(row)
        
        print("Given matrix:")
        for row in A:
            print(row)

        for i in range(n):
            diag_index = n - i - 1          
            min_index = find_min_index(A[i])  
            A[i][diag_index], A[i][min_index] = A[i][min_index], A[i][diag_index]

        print("Result:")
        for row in A:
            print(row)

    if task == 2:
        i = 1
        trains = []
        while True:
            add_type = input("Add new train? (y/n): ")
            if add_type != 'y':
                break

            day = input(f"Input train#{i} arrival date: ")
            try:
                day = int(day)
            except ValueError:
                print("Error: day is not an integer")
                break

            num = input(f"Input train#{i} number: ")
            try:
                num = int(num)
            except ValueError:
                print("Error: number is not an integer")
                break

            destination = input(f"Input train#{i} destination: ")
            departure_time = input(f"Input train#{i} departure time (HH:MM): ")
            arrival_time = input(f"Input train#{i} arrival time (HH:MM): ")

            train = {
                "day": day,
                "number": num,
                "destination": destination,
                "departure_time": departure_time,
                "arrival_time": arrival_time
            }

            trains.append(train)
                
            i += 1

        search_day = input("Input day for search: ")
        try:
            int(search_day)
        except ValueError:
            print("Error: day is not integer")
        if search_day < 1 or search_day > 31:
                print("Error: day is out of range")
                break

        for train in trains:
            if train["day"] == search_day:
                print(f"Train number: {train["number"]}")
                print(f"Train destination: {train["destination"]}")
                print("\n")
            else:
                print("There are no trains on")

    if task == 3:
        states_candidates = {
            "Alabama": {
                "Donald J. Trump": 0,
                "Kamala D. Harris": 0,
                "Jill Stein": 0
            },
            "Alaska": {
                "Chase Oliver": 0,
                "Cornel West": 0,
                "Robert F. Kennedy Jr.": 0
            },
            "Arizona": {
                "Randall Terry": 0, 
                "Clifton Roberts": 0,
                "Jasmine Sherman": 0
            },
            "Arkansas": {
               "Hunter F. Roberts": 0,
               "Michael Delaney": 0,
               "Dennis Knickmeyer": 0
            },
            "California": {
                "Joe Biden": 0,
                "Gloria La Riva": 0,
                "Brian Carroll": 0
            }
        }

        while True:
            choice = input("Do you want to input votes? (y/n): ")
            if choice not in ['y', 'n']:
                print("Error: invalid input")
                break
            elif choice == 'n':
                break

            state = input("Input state: ")

            if state not in states_candidates:
                print("State is not found")
                continue

            for candidate in states_candidates[state]:
                votes = input(f"Input number of votes for {candidate}: ")
                try:
                    votes = int(votes)
                except ValueError:
                    print("Error: number of votes is not integer")
                    exit()

                if votes < 0:
                    print("Error: votes cannot be negative")
                    break

                states_candidates[state][candidate] = votes

            total_votes = {}

            for state in states_candidates:
                for candidate, votes in states_candidates[state].items():
                    if candidate not in total_votes:
                        total_votes[candidate] = 0
                    total_votes[candidate] += votes

            print("\nTotal votes across all states:")
            for candidate in sorted(total_votes.keys()):
                print(f"{candidate}: {total_votes[candidate]}")

        president = max(total_votes, key=total_votes.get)
        print("\nElected president nationwide:", president)
