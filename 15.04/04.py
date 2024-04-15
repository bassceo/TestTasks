arr = ['aa', 'a', 'bbb', 'cccc']

print(sorted(arr,key=lambda x: len(x)))

print(sorted(arr,key=lambda x: len(x), reverse=True))