def Q(lt, rt):
  if lt < rt:
    pivot = arr[rt]
    pos = lt
    for i in range(lt, rt):
      if arr[i] <= pivot:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
    arr[pos], arr[rt] = arr[rt], arr[pos]

    Q(lt, pos - 1)
    Q(pos + 1, rt)

arr = [45,21,23,36,15,67,11,60,20,33]
print("before arr = ",arr)
Q(0,9)
print("after arr = ",arr)