def find_min_index(row):
    min_index = 0
    for i in range(1, len(row)):
        if row[i] < row[min_index]:
            min_index = i
    return min_index


while True:
    task = int(input("Input task: "))
    if task == 1:
        n = int(input("Input n: "))
        if type(n) != int:
            print("Error: n is not an integer")
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
                num = int(input(f"Input train#{i} number: "))
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

            search_day = int(input("Input day for search: "))
            if search_day < 1 or search_day > 31:
                print("Error: day is out of range")
                exit()

            for train in trains:
                if train["day"] == search_day:
                    print(f"Day of arrival: {train["day"]}")
                    print(f"Train number: {train["number"]}")
                    print(f"Train destination: {train["destination"]}")
                    print(f"Train arrival time: {train["arrival_time"]}")
                    print(f"Train departure time: {train["departure_time"]}")
                    print("\n")
                else:
                    print("There are no trains on")

        if task == 3:
            states_candidates = []
            washington_candidates_votes = {
                "Abraham Lincoln": 0,
                "John F. Kennedy": 0,
                "F. D. Roosevelt": 0,
            }
            illinois_candidates_votes = {
                "Donald Trump": 0,
                "John Adams": 0,
                "Thomas Jefferson": 0
            }
            states_candidates.append(washington_candidates_votes)
            states_candidates.append(illinois_candidates_votes)
            
            state = input("Input state: ")
            if state != "Washington" and state != "Illinois":
                print(f"Error: there are no candidates from {state}")
            elif (state == "Washington"):
                candidates = list(washington_candidates_votes.keys)
                print("Candidates in Washington:")
                i = 1
                for candidate in candidates:
                    print({i}, ".", candidate, end="\n")
                    i += 1
                chosen_candidate = int(input("Input candidate number: "))
                number_of_votes = int(input("Input number of votes: "))
                
