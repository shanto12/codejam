# def difference_calculator(arr):
#     N = arr[0]
#     indicator_1 = indicator_2 = 0
#
#     index = 1
#
#     while 1 and index <= N:
#         k = arr[index]
#         starting_index = index
#         occurrences = 0
#         while index <= N and arr[index] == k:
#             index += 1
#             occurrences += 1
#         if k == occurrences:
#             indicator_1 += 1
#         if k == occurrences and k == starting_index:
#             indicator_2 += 1
#
#     return abs(indicator_1 - indicator_2)


# def segment(x, space):
#     # Write your code here
#     N = len(space)
#     minima_of_segments = []
#
#     for index in range(N):
#         if index + x <= N:
#             minima_of_segments.append(min(space[index: index + x]))
#
#
#     # for index in range(N-x):
#     #     minima_of_segments.append(min(space[index: index + x]))
#
#
#
#
#
#     # index = 0
#     # flag = True
#     # while flag and index < N:
#     #     if index + segment_length < N:
#     #         minima_of_segments.append(min(space[index: index + segment_length]))
#     #         index += segment_length
#     #     elif index == N - 1:
#     #         flag = False
#     #     else:
#     #         segmentx = space[index: (index + min(index + segment_length, N - 1))]
#     #         minima_of_segments.append(min(segmentx))
#     #
#     #         flag = False
#
#     return max(minima_of_segments)


def getUnallottedUsers(bids, totalShares):
    # Write your code here
    looser_id_list = [x[0] for x in bids]
    user_dict = dict()
    for bid in bids:
        user_dict.setdefault(bid[2], dict())
        user_dict[bid[2]].setdefault(bid[3], dict())
        user_dict[bid[2]][bid[3]] = {"id": bid[0], "shares": bid[1]}


    for price, ts_dict in sorted(user_dict.items(), reverse=True):
        if len(ts_dict)==1:
            for ts, details_dict in ts_dict.items():
                totalShares-= details_dict.get("shares")
                looser_id_list.remove(details_dict.get("id"))
        elif totalShares>=len(ts_dict):
            for ts, details_dict in ts_dict.items():
                looser_id_list.remove(details_dict.get("id"))
        else:
            for ts, details_dict in sorted(ts_dict.items(), reverse=True):
                looser_id_list.remove(details_dict.get("id"))
                totalShares-=1
                if totalShares==0:
                    break


    return looser_id_list


x = """
10
1
2
2
4
4
4
4
2
2
2
"""

value = getUnallottedUsers([[1, 3, 1, 9866],[2, 1, 2, 5258],[3, 2, 4, 5788],[4, 2, 4, 6536]], 4)

print(value)
