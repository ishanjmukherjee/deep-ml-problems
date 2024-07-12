def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if len(a) != len(b):
      return -1
    c = [sum(aCol * bRow for aCol, bRow in zip(aRow, b)) for aRow in a]
    return c
