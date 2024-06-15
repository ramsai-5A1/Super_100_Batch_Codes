

class Solution(object):
    def asteroidCollision(self, asteroids):
        positive, negative = [], []
        result = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                positive.append(asteroid)
            else:
                value = abs(asteroid)
                shouldInsertAsteroid = True
                while True:
                    if len(positive) == 0:
                        break 
                    
                    if positive[-1] == value:
                        positive.pop()
                        shouldInsertAsteroid = False
                        break 
                    
                    if positive[-1] < value:
                        positive.pop()
                    else:
                        shouldInsertAsteroid = False
                        break
                    
                if shouldInsertAsteroid:
                    negative.append(value)
                    
        for ele in negative:
            result.append(-1 * ele)
            
        for ele in positive:
            result.append(ele)
        return result
        
        
