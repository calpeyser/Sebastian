def get_only_element(a):
    if len(a) != 1:
        raise Exception("List must have one element")
    return a[0]