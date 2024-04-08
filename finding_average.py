def average(array):
    array=set(array)
    array=list(array)
    av = sum(array)/len(array)
    return av

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
