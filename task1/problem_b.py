n = int(input())
marks = input()

marks = [int(mark) for mark in marks.strip().split()]

def insertion_sort(lst):
    result = [lst[0]]
    for i in range(1, len(lst)):
        new_element = lst[i]
        for j, old_element in enumerate(result):
            if new_element < old_element:
                result.insert(j, new_element)
                break
        if len(result) == i:  # new element wasn't inserted yet
            result.append(new_element)
    return result

rating = insertion_sort([(-mark, number) for number, mark in enumerate(marks)])
print(" ".join([str(number + 1) for _, number in rating]))
