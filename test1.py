def find_once_in_order(gong_pai):
    strs = gong_pai.split(" ")
    n = len(strs)
    existed = set()
    for i in range(n):
        for j in range(i + 1, n):
            if strs[i] == strs[j]:
                existed.add(strs[i])
                break
        if strs[i] not in existed:
            return strs[i]
    return ""


assert find_once_in_order("A1 B2 A1 C3 B2") == "C3"
assert find_once_in_order("X1 X1 Y2 Y2") == ""
assert find_once_in_order("K9 K8 K9") == "K8"
