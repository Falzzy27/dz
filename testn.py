with open(r"C:\Users\slano\PycharmProjects\pythonProject3\file.txt", 'r') as f:
    len_s = int(f.readline()) + 1
    lines = [int(i.strip()) for i in f.readlines()] + [-1 * 10 ** 10]
    k = last_sum = 0
    for i in range(1, len_s):
        if lines[i - 1] < lines[i]:
            k += 1
        else:
            summ = sum(lines[i - k - 1: i])
            k = 0
    print(summ)
