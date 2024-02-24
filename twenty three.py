def my_filter(a):
    string = ""
    for i in a:
        string += str(i * 10) + " "
    return string
a = list(map(int, input().split()))
print(my_filter(a))