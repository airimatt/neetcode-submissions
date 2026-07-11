class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # first store: user : list of websites
        # then go through each user's list and get patterns
        # store pattern : set of users

        arr = list(zip(timestamp, username, website))
        arr.sort()

        userMap = defaultdict(list)

        for time, user, site in arr:
            userMap[user].append((time, site))
        
        patternMap = defaultdict(set)

        for user in userMap:
            websites = userMap[user]
            for i in range(len(websites) - 2):
                pattern = (websites[i][1], websites[i + 1][1], websites[i + 2][1])
                patternMap[pattern].add(user)
        
        maxUsers = 0
        res = None
        for pattern, users in patternMap.items():
            if len(users) > maxUsers:
                maxUsers = len(users)
                res = pattern
            elif len(users) == maxUsers:
                if res > pattern:
                    res = pattern

        return list(res)