# # text = input()
# # regex = input()



# # def is_match(substring, pat):
# #     i, j = 0, 0
# #     while i < len(substring) and j < len(pat):
# #         if pat[j] == '*':
# #             return True
# #         if substring[i] != pat[j]:
# #             return False
# #         i += 1
# #         j += 1
# #     return j == len(pat)

# # def getLongestMatch(text, regex):

# #     parts = 

# #     prefix, suffix = parts
# #     max_length = 0

# #     for i in range(len(text)):
# #         if text[i:].startswith(prefix):
# #             for j in range(len(text), i + len(prefix), -1):
# #                 if text[j:].startswith(suffix):
# #                     length = j - i + len(suffix)
# #                     if length > max_length:
# #                         max_length = length

# #     return max_length if max_length else -1

# # print(getLongestMatch(text, regex))


text = input()
regex = input()



# def is_match(substring, pat):
#     i, j = 0, 0
#     while i < len(substring) and j < len(pat):
#         if pat[j] == '*':
#             return True
#         if substring[i] != pat[j]:
#             return False
#         i += 1
#         j += 1
#     return j == len(pat)

def getLongestMatch(text, regex):
    prefix, suffix = regex.split('*')

    lt = len(text)
    lp = len(prefix)
    ls = len(suffix)
    i=0

    while i < lt:
        if text[i:].startswith(prefix):
            break
        i += 1

    j = lt
    while j > i + lp:
        if text[j:].startswith(suffix):
            length = j - i + ls
            return length
        j -= 1

    return -1

text.rfind()

print(getLongestMatch(text, regex))



# def getLongestMatch(text: str, regex: str) -> int:
#     parts = regex.split('*')
#     if len(parts) != 2:
#         return -1
#     pre, su = parts
#     pre_len = len(pre)
#     su_len = len(su)
#     n = len(text)
#     if pre_len + su_len > n:
#         return -1
#     start = []
#     for i in range(n - pre_len + 1):
#         if text[i:i + pre_len] == pre:
#             start.append(i)
#     end = []
#     for i in range(su_len, n + 1):
#         if text[i - su_len:i] == su:
#             end.append(i)
#     ml = -1
#     j = 0
#     for i in start:
#         while j < len(end) and end[j] < i + pre_len:
#             j += 1
#         if j < len(end):
#             ml = max(ml, end[j] - i)
#     return ml

# text = str(input())
# regex = str(input())
# print(getLongestMatch(text,regex))