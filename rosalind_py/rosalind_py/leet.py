import itertools
import math

def longestSubstring(s): 
    result, cur_max = 0, 0
    d = {}

    if len(s) == 1: return 1

    for i in range(len(s)): 
        if d.get(s[i], None) == None:
            d[s[i]] = True # just set it to something 
            cur_max += 1
        else: 
            if cur_max > result: result = cur_max 
            d = {s[i]: True}
            cur_max = 1

    if result > cur_max: return result
    else: return cur_max

def substring2(s): 
    result, cur_max = 0, 0
    d = {}

    for i in range(len(s)): 
        for j in range(i, len(s)):
            if d.get(s[i], None) == None: 
                d[s[i]] = True
                cur_max += 1
            else: 
                if cur_max > result: 
                    result = cur_max
                d = {}
                cur_max = 0

    if result > cur_max: return result
    else: return cur_max

def median(l1, l2): 
    if len(l2) == 0: 
        if len(l1) == 1: return l1[0]
        elif len(l1) % 2 == 0: return (l1[int(len(l1)/2)]+l1[int(len(l1)/2)-1])/2.0
        else: return l1[int(len(l1)/2)]
    elif len(l1) == 0: 
        if len(l2) == 1: return l2[0]
        elif len(l2) % 2 == 0: return (l2[int(len(l2)/2)]+l2[int(len(l2)/2)-1])/2.0
        else: return l2[int(len(l2)/2)]
    # next two are based on sorted assumption
    elif l1[0] <= l2[0]: 
        return (l1[0] + l2[-1]) / 2.0
    elif l2[0] <= l1[0]: 
        return (l1[-1] + l2[0]) / 2.0

def atoi(string): 
    "Status: Accepted"
    string = string.strip()
    result = []
    sym = 0

    for char in string: 
        if char == "+" or char == "-": 
            if sym == 0: 
                if char == "+": sym = 1 
                else: sym = -1
            else: 
                return 0 
        elif char.isdigit(): 
            result.append(char)
        else: 
            break; 

    result = "".join(result) 
    if result: 
        result = int(result)
        if sym != 0: result *= sym 
        if result > 2147483647: return 2147483647
        elif result < -2147483648: return -2147483648
        else: return result 
    else: return 0

def atoi3(s): 
    """Converts a string to an integer 

    Parameters
    -----------
    s (str): A string

    Returns
    -------
    int: s as an integer
    """
    if s == " " or s == "" or s == "+" or s == "-": return 0

    s = s.strip()
    result = []
    sym, canary = 1, 0

    for i in range(len(s)-1, -1, -1): 
        if s[i].isdigit() and canary == 0: 
            result.insert(0, s[i])
        elif s[i] == "-" or s[i] == "+": 
            if canary == 0 and s[i] == "-": sym, canary = -1, 1
            elif canary == 0 and s[i] == "+": sym, canary = 1, 1
            else: return 0
        else: 
            return 0 

    return int("".join(result)) * sym

def atoi2(s): 
    result = 0
    sym = 1
    first_digit = 0 
    period_position = 0

    for i in range(len(s)): 
        if s[i].isdigit(): 
            first_digit = i 
            break 
        elif s[i] == ".": period_position = i 
        elif s[i] == "+": sym = 1
        elif s[i] == "-": sym = -1 
        else: return None # ran into a bad characters


    if period_position == 0: period_position = -1 

    print("period_position: {}, first_digit: {}".format(period_position, -(len(s) - first_digit+1)))
    for i in range(-period_position, -(len(s)-first_digit), -1): 
            print("{}, {}".format(i, s[i]))
            result *= 10 
            result += int(s[i])
    
    return result * sym

def isNumPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 <= x <= 9: return True
        elif -9 <= x <= -1: return False
        
        result = 0
        tmp = x
        
        while tmp > 0: 
            result *= 10
            result += tmp % 10
            tmp = tmp // 10
            
        return result == x

def getLongestStringFromList(str_list): 
    longest_string = ""
    longest_length = 0
    i = 0 

    # Get the longest string from the list 
    for i in range(len(str_list)): 
        if len(str_list[i]) > longest_length: 
            longest_string = str_list[i] 
            longest_length = len(str_list[i])
    return longest_string

def longestCommonPrefix(str_list):
    # TODO: Refactor this to use a while loop 
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(str_list) == 0: return ""
    longest_string = ""
    longest_length = 0
    longest_index = 0 

    for i in range(len(str_list)): 
        if len(str_list[i]) > longest_length: 
            longest_string = str_list[i] 
            longest_length = len(str_list[i])
            longest_index = i

    str_list.pop(longest_index)

    canary = 0
    for string in str_list: 
        if string.startswith(longest_string) != False: 
            continue
        else: 
            canary = -1 

    if canary == 0: 
        return longest_string 

    for i in range(-1, -(len(longest_string)), -1): 
        canary = 0
        print("Longest String: {}".format(longest_string[:i]))
        for string in str_list: 
            if string.startswith(longest_string[:i]) != False: 
                continue 
            else: 
                canary = -1
                break 

        if canary == 0: 
            return longest_string[:i]

    return ""
    

def regexMatch(s, pat): 
    i, j = 0, 0 
    lenPat, lenS = len(pat), len(s)

    while i < lenPat: 
        if i + 1 < lenPat and pat[i+1] == "*" and pat[i] == ".": 
            i, j = i+2, lenS 
            break 
        elif i + 1 < lenPat and pat[i+1] == "*": 
            while j < lenS and pat[i] == s[j]: j += 1
            tmp_char = pat[i]
            i += 2
            while i < lenPat and i+1< lenPat and pat[i+1] == "*": 
                if j >= lenS or pat[i] != s[j]: i += 2
                else: break 
            while i < lenPat and pat[i] == tmp_char: i += 1

        elif j < lenS and pat[i] == s[j] or pat[i] == ".": i, j = i+1, j+1
        else: return False

    while i < lenPat and i+1 < lenPat and pat[i+1] == "*": 
        if pat[i] == s[-1]: i += 2
        else: break 

    if i < lenPat and lenS > 0 and pat[i] == s[-1]: i += 1

    while i < lenPat and pat[i] == ".": i += 1

    if i >= lenPat and j >= lenS: return True 
    else: return False

def validParen(string): 
    stack = []
    for char in string: 
        if char == "(" or char == "{" or char == "[": 
            stack.append(char)
        elif char == ")": 
            if len(stack) == 0: return False
            tmp = stack.pop() 
            if tmp == "(": continue 
            else: return False
        elif char == "}": 
            if len(stack) == 0: return False
            tmp = stack.pop() 
            if tmp == "{": continue 
            else: return False
        elif char == "]": 
            if len(stack) == 0: return False
            tmp = stack.pop() 
            if tmp == "[": continue 
            else: return False
        else: continue 

    return len(stack) == 0

def threeSum(self, num_list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        items = itertools.combinations(num_list, 3)
        for item in items: 
            item = sorted(list(item))
            if item not in result and sum(item) == 0: 
                    result.append(item)
    
        return result

def threeSumClosest(self, nums, target):
    result = 0
    target = abs(target)
    distance = None

    items = itertools.combinations(nums, 3)
    for item in items: 
        tmp_distance = abs(sum(item) - target)
        if tmp_distance == 0: return sum(item)
        elif distance == None or tmp_distance < distance: 
            distance = tmp_distance 
            result = sum(item)
    return result

class ListNode: 
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        q = []
        node = head
        
        while node: 
            q.append(node) 
            node = node.next
            
        if n+1 > len(q): 
            q.pop(0)
        elif n == 1: 
            q.pop()
            q[-1].next = None
        else: 
            q[-n-1].next = q[-n+1]
            
        if len(q) == 0: return None
        else: return q[0]

def integerToEnglishWords(n): 
    d = (("one", "ten", "eleven"), ("two", "twenty", "twelve"), ("three", "thirty", "thirteen"), ("four", "forty", "fourteen"), 
         ("five", "fifty", "fifteen"), ("six", "sixty", "sixteen"), ("seven", "seventy", "seventeen"), ("eight", "eighty", "eighteen"), 
         ("nine", "ninety", "nineteen"))

    result = []
    num_list = []

    if n == 0: return "Zero"

    while n > 0: 
        i = n % 10 
        n = n // 10 
        if i == 0: 
            num_list.append(i)
            continue 
        l = len(num_list) 
        if l == 0: # ones
            result.insert(0, d[i-1][0].title())
        elif l == 1: # tens
            if i == 1: 
                if num_list[-1] == 0: 
                    result.insert(0, d[0][1].title()) # append a ten 
                else: # insert a *teen number
                    result.pop(0)
                    result.insert(0, d[num_list[-1]-1][2].title())
            else: 
                result.insert(0, d[i-1][1].title())
        elif l == 2: # hundreds
            result.insert(0, "Hundred")
            result.insert(0, (d[i-1][0]).title())
        elif l == 3: # Thousands
            result.insert(0, "Thousand")
            result.insert(0, (d[i-1][0]).title())
        elif l == 4: # Ten thousands
            if num_list[-1] == 0: result.insert(0, "Thousand") 
            if i == 1: 
                if num_list[-1] == 0: 
                    result.insert(0, d[0][1].title()) # append a ten 
                else: # insert a *teen number
                    result.pop(0)
                    result.insert(0, d[num_list[-1]-1][2].title())
            else: 
                result.insert(0, d[i-1][1].title())

        elif l == 5: # hundred thousands
            if num_list[-1] == 0 and num_list[-2] == 0: result.insert(0, "Thousand") 
            result.insert(0, "Hundred")
            result.insert(0, (d[i-1][0]).title())
        elif l == 6: # Millions
            result.insert(0, "Million")
            result.insert(0, (d[i-1][0]).title())

        elif l == 7: # Ten Millions
            if num_list[-1] == 0: result.insert(0, "Million") 
            if i == 1: 
                if num_list[-1] == 0: 
                    result.insert(0, d[0][1].title()) # append a ten 
                else: # insert a *teen number
                    result.pop(0)
                    result.insert(0, d[num_list[-1]-1][2].title())
            else: 
                result.insert(0, d[i-1][1].title())

        elif l == 8: # hundred thousands
            if num_list[-1] == 0 and num_list[-2] == 0: result.insert(0, "Million") 
            result.insert(0, "Hundred")
            result.insert(0, (d[i-1][0]).title())
        elif l == 9: # Millions
            result.insert(0, "Billion")
            result.insert(0, (d[i-1][0]).title())

        num_list.append(i)

    return " ".join(result)

def arrayIntersection(nums1, nums2): 
    """Returns the intersection of two arrays"""
    result = []
    for val in nums1: 
        if val in nums2 and val not in result: 
            result.append(val)
    return result

def arrayIntersectionTwo(nums1, nums2): 
    if len(nums1) < len(nums2): 
            small_arr = nums1 
            long_arr = nums2
        else: 
            small_arr = nums2
            long_arr = nums1
            
        result = []
            
        for val in small_arr: 
            try: 
                i = long_arr.index(val)
                result.append(val)
                long_arr.pop(i)
            except ValueError: 
                pass
            
        return result 

if __name__ == "__main__": 
    pass
    










