from typing import List


class Solution:

    # ------------ using dp --------------
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        used_arr = [True] * len(tasks)
        globalResult = {}
        return self.findMinSession(
            tasks, len(tasks), used_arr, globalResult, sessionTime)[0]

    def findMinSession(self, tasks, tasksNum, used_arr,
                       globalResult, sessionTime):
        flag = self.translate(used_arr)
        if flag in globalResult:
            return globalResult[flag]
        if tasksNum == 0:
            return (1, 0)
        ans = (float("inf"), float("inf"))
        for i in range(len(used_arr)):
            if used_arr[i]:
                used_arr[i] = False
                (sessionNum, usedSessionPart) = self.findMinSession(
                    tasks, tasksNum - 1, used_arr, globalResult, sessionTime)
                oversized = (tasks[i] + usedSessionPart) > sessionTime
                ans = min(ans, (sessionNum + oversized,
                                tasks[i] + usedSessionPart * (1 - oversized)))
                used_arr[i] = True
        globalResult[flag] = ans
        return ans

    def translate(self, used_arr):
        temp = [0] * len(used_arr)
        for i in range(len(used_arr)):
            if used_arr[i]:
                temp[i] = '1'
            else:
                temp[i] = '0'
        res = ''.join(temp)
        return res

    # ------------ put tasks in sessions - iterate sessions rather than the ta
    # def minSessions(self, tasks: List[int], sessionTime: int) -> int:
    #     tasks.sort(reverse=True)
    #     sessions = []
    #     result = [0]

    #     self.fillTheSessions(tasks, sessions, 0, sessionTime, result)
    #     return result[0]

    # def fillTheSessions(self, tasks, sessions, currentTask, sessionTime, result):
    #     if currentTask == len(tasks):
    #         result[0] = min(len(sessions), result[0])
    #         return result[0]

    #     for i in range(len(sessions)):
    #         if sessions[i] + tasks[currentTask] <= sessionTime:
    #             sessions[i] += tasks[currentTask]
    #             self.fillTheSessions(tasks, sessions, currentTask + 1, sessionTime, result)
    #             sessions[i] -= tasks[currentTask]

    #     sessions.append(tasks[currentTask])
    #     self.fillTheSessions(tasks, sessions, currentTask + 1, sessionTime, result)
    #     sessions.pop()

    # ------------ using recursive and memorization --------------
    # def minSessions(self, tasks: List[int], sessionTime: int) -> int:
    #     used_arr = [False] * len(tasks)

    #     globalResult = {}

    #     num =  self.findSubMinSession(tasks, used_arr, 0, 1, 0, sessionTime, globalResult)
    #     return num

    # def findSubMinSession(self, tasks, used_arr, usedNum, currentSessionNum, usedSessionPart, sessionTime, globalResult):
    #     minNums = 1111111

    #     flag = self.translate(used_arr, currentSessionNum, usedSessionPart)

    #     if usedNum in globalResult and currentSessionNum in globalResult[usedNum] and flag in globalResult[usedNum][currentSessionNum]:
    #         return globalResult[usedNum][currentSessionNum][flag]

    #     if usedNum == len(tasks):
    #         if usedSessionPart == 0:
    #             return currentSessionNum - 1
    #         return currentSessionNum

    #     for i in range(len(used_arr)):
    #         if not used_arr[i]:
    #             used_arr[i] = True
    #             numbers = minNums
    #             tempNum = sessionTime - usedSessionPart
    #             if tempNum > tasks[i]:
    #                 numbers = self.findSubMinSession(tasks, used_arr, usedNum + 1, currentSessionNum, usedSessionPart + tasks[i], sessionTime, globalResult)
    #             elif tempNum == tasks[i]:
    #                 numbers = self.findSubMinSession(tasks, used_arr, usedNum + 1, currentSessionNum + 1, 0, sessionTime, globalResult)
    #             else:
    #                 numbers = self.findSubMinSession(tasks, used_arr, usedNum + 1, currentSessionNum + 1, tasks[i], sessionTime, globalResult)

    #             if numbers < minNums:
    #                 minNums = numbers
    #             used_arr[i] = False

    #     if usedNum not in globalResult:
    #         globalResult[usedNum] = {}
    #     if currentSessionNum not in globalResult[usedNum]:
    #         globalResult[usedNum][currentSessionNum] = {}
    #     globalResult[usedNum][currentSessionNum][flag] = minNums

    #     return minNums

    # def translate(self, used_arr, currentSessionNum, current_session):
    #     temp=[0] * len(used_arr)
    #     for i in range(len(used_arr)):
    #         if used_arr[i]:
    #             temp[i] = '1'
    #         else:
    #             temp[i] = '0'
    #     res = ''.join(temp)
    #     res += str(current_session)
    #     return res
