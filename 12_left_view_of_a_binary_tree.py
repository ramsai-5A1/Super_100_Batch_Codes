def LeftView(root):
    result = []
    if root == None:
        return result

    Q = []
    Q.append(root)

    while Q:
        n = len(Q)
        for i in range(n):
            current = Q.pop(0)
            if i == 0:
                result.append(current.data)

            if current.left != None:
                Q.append(current.left)

            if current.right != None:
                Q.append(current.right)

    return result
