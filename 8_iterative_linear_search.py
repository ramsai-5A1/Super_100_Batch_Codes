def search(self,arr, N, X):
        result = -1 
        for index in range(N):
            if arr[index] == X:
                result = index 
                break
        return result
