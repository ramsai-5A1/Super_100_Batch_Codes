class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)
        if n % groupSize != 0:
            return False 

        store = dict()
        for ele in hand:
            store[ele] = store.get(ele, 0) + 1 

        keys = sorted(store.keys())
        while keys:
            value = keys[0]
            mn = store[value]
            for i in range(groupSize):
                curr = value + i 
                if curr not in store or store[curr] < mn:
                    return False 
                store[curr] -= mn 
                if store[curr] == 0:
                    store.pop(curr)
                    keys.pop(keys.index(curr))
                
        return True