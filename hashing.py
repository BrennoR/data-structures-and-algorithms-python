def hash(astring, tablesize):
    sum = 0
    for c in astring:
        sum += ord(c)

    return sum % tablesize


def hash_2(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += (ord(astring[pos]) * (pos + 1))

    return sum % tablesize


print(hash('cat', 11))
print(hash_2('cat', 11))
