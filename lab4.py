while True:
    #Variant 6
    task = int(input("Input task: "))
    if task == 1:
        F1 = r"D:\python_labs\lab4\F1.txt" 
        F2 = r"D:\python_labs\lab4\F2.txt"

        f1 = open(F1, 'r')
        f2 = open(F2, 'w')

        numbers = f1.read().split()

        print("Elements written in F2.txt:")
        for i in range(len(numbers)):
            try:
                num = int(numbers[i])
                if num < 0 and i % 2 != 0:
                    f2.write(str(num) + " ")
                    print(num)
            except ValueError:
                continue

        f1.close()
        f2.close()
    
    elif task == 2:
        #Variant 8
        s1 = int(input("Input s1: "))
        s2 = int(input("Input s2: "))
        k = int(input("Input k: "))
        n = int(input("Input n: "))
        textfile = r"D:\python_labs\lab4\text.txt"
        txt = open(textfile, 'r')
        lines = txt.readlines()
        print("Lines:")
        count = 0
        for line in lines:
            if count == 0:
                print("First symbol of first line: ", line.strip()[0])
                print("Fifth symbol of first line: ", line.strip()[4])
                print("First 10 symbols of first line: ")
                for i in range(10):
                    print(line.strip()[i])
                print(f"Symbols of first line in range [{s1}, {s2}]")
                for i in range(s1, s2):
                    print(line.strip()[i])
            if count == 1:
                print("First symbol of second line: ", line.strip()[0])
            if count == n:
                print(f"Symbol at index {k} in line {n}:", line.strip()[k])
            count += 1


    elif task == 0:
        print("Exiting the program.")
        exit()
