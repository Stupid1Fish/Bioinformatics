def hamming(text1,text2):
    number = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            number += 1
    return number

def hamming_pattern(pattern, text, d):
    c = 0
    for i in range(len(text) - len(pattern)+1):
        pattern_intext = text[i : i+len(pattern)]
        if hamming(text1=pattern, text2=pattern_intext) <= d :
            c += 1
            print(c)

pattern = "AAAAA"
text  ="AACAAGCTGATAAACATTTAAAGAG"
d = 2
hamming_pattern(pattern, text, d)