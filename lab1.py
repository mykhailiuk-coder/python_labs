from math import factorial

while True:
    task = int(input("Enter task: "))
    if task == 1:
        a = float(input("Enter a: "))
        x = float(input("Enter x: "))
        if x == 0 or a == 0:
            print("Error: a or x is zero")
            exit()

        epsilon = float(input("Enter epsilon: "))
        if epsilon <= 0:
            print("Error: epsilon is negative")
            exit()

        accuracy = int(input("Enter accuracy(number of digits after coma): "))
        if accuracy <= 0:
            print("Error: accuracy is not positive")
            exit()

        k = 1
        addedSum = 0
        count = 0

        while True:
            result = (((-1)**k) * (x ** (-4*k))) / (a**4 + factorial(k))
            addedSum += result
            k += 1
            count += 1
            if abs(result) < epsilon:
                break

        print("Result:", round(addedSum, accuracy))
        print("Count:", count)

    if task == 2:
        x = float(input("Enter x: "))
        epsilon = float(input("Enter epsilon: "))
        if epsilon <= 0:
            print("Error: epsilon is not positive")
            exit()

        a = [x]

        print("Result:\n")
        for i in range(1, 100):
            next_a = 4 * a[-1] / 5 + x / (5 * a[-1] ** 4)
            a.append(next_a)
            print(f"a[{i}] = {next_a}")
            if abs(a[i] - a[i - 1]) < epsilon:
                print(a[i], "at index:", i)
                break

    if task == 3:
        text = input("Enter text: ")
        words = text.split()
        unique_words = []

        for word in words:
            if word not in unique_words:
                unique_words.append(word)

        print("Unique words:")
        for word in unique_words:
            print(word)

    if task == 4:
        

    if task == 0:
        print("Exiting...")
        exit()
