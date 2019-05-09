from itertools import product

def frequency(text, k, d):
    nums = []
    patterns = []
    str = ""
    nucleotides = "ATGC"
    for i in list(product(nucleotides, repeat = k )):  #生成 4^k的组合，并join
        patterns.append(str.join(i))

    for pattern in patterns:
        num = hamming_pattern(text, pattern, d)
        nums.append(num)

    max_num = max(nums)
    for i in range(len(nums)):
        if nums[i] == max_num:
            print(patterns[i], end=" ")



def hamming(text1,text2):  #对比两段
    number = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            number += 1
    return number

def hamming_pattern(text, pattern, d):  # 每个pattern 汉明距离小于d的数目
    num = 0

    for i in range(len(text) - len(pattern) + 1):
        pattern_intext = text[i : i + len(pattern)]
        if hamming(text1=pattern, text2=pattern_intext) <= d :
            num += 1
    return num

text = "CACTCGTACCGTGACACCACGTGATTCGTGATCGTACCTTCGTGACACACCGTGATCGTACCTCGTACCGTGAACCTTCACCCACTCGTGTGATCGTTCGTTTCTTCACCCACTTCGTGAACCTTCTTCTTCACCGTGATCGTTTCACCACCCACTTCGTGAGTGACACGTGATCGTTTCGTGACACTTCTCGTTCGTTTCTTCACCACCCACGTGATCGTTCGTCACCACTCGTTTCACCTCGTCACGTGAACCGTGAACCTTCTCGTGTGAACCTTCGTGACACACCGTGACACTTCCACTCGTCACTCGTCACACCGTGATTCGTGAGTGAGTGATCGTACCTCGTGTGATCGTGTGATTCACCTCGT"


k = 6
d = 3
frequency(text, k, d)