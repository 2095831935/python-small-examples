# 去掉最高分、最低分求平均

#方法1：
def score_mean(lst):
    lst.sort()
    lst_2=lst[1:(len(lst)-1)]
    return round((sum(lst_2)/len(lst_2)),1)

lst=[9.1, 9.0,8.1, 9.7, 19,8.2, 8.6,9.8]
score_mean(lst)

#方法2:
lst.remove(min(lst))
lst.remove(max(lst))
print(lst)
print(round(sum(lst)/len(lst),1))