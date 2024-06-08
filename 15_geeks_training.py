class Solution:
    def maximumPoints(self, points, n):
        def recursiveApproach(day, prevDayOption):
            if day == n:
                return 0 
                
            result = 0 
            for option in range(3):
                if option != prevDayOption:
                    currResult = points[day][option] + recursiveApproach(day + 1, option)
                    result = max(result, currResult)
            return result
        
        
        # day --> 0 to n - 1 
        # prevDayOption --> -1, 0, 1, 2  --> 0 1 2 3 
        # n = 5 
        
        cache = []
        for i in range(n + 1):
            eachRow = [-1] * 4 
            cache.append(eachRow)
        
        
        def memoizationApproach(day, prevDayOption):
            if day == n:
                return 0 
            elif cache[day][prevDayOption + 1] != -1:
                return cache[day][prevDayOption + 1]
            result = 0 
            for option in range(3):
                if option != prevDayOption:
                    currResult = points[day][option] + memoizationApproach(day + 1, option)
                    result = max(result, currResult)
                    
            cache[day][prevDayOption + 1] = result
            return result
        
        def tabulationApproach():
            # From memoization to tabulation we need to follow below steps:
            # 1 - Convert all base conditions to initializations in cache 
            # 2 - Write the for loop  
            # 3 - Copy paste the core-logic of memoization function
            # 4 - Change the function-call name to cache 
            
            cache[n][0] = 0 
            cache[n][1] = 0 
            cache[n][2] = 0 
            #cache[n][3] = 0 
            
            for day in range(n - 1, -1, -1):
                # for prevDayOption in range(3):
                #     result = 0 
                #     for option in range(3):
                #         if option != prevDayOption:
                #             currResult = points[day][option] + cache[day + 1][option]
                #             result = max(result, currResult)
                #     cache[day][prevDayOption] = result
                cache[day][0] = points[day][0] + max(cache[day + 1][1], cache[day + 1][2])
                cache[day][1] = points[day][1] + max(cache[day + 1][0], cache[day + 1][2])
                cache[day][2] = points[day][2] + max(cache[day + 1][0], cache[day + 1][1])
            #print(cache)   
            return max([cache[0][0], cache[0][1], cache[0][2]])
            
        
        return tabulationApproach()
