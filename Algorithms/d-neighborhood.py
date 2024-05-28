def nei(pattern):
    neighborhood = [pattern]
    nucleotides = "ATCG"
    for i in range(len(pattern)) :
        symbol = pattern[i]
        nu_exce = nucleotides.replace(symbol,"")
        for x in nu_exce:
            neighbor =  pattern[:i] + x + pattern[i+1:]
            neighborhood.append(neighbor)
    k = 0
    for c in neighborhood:
        k = k+1
        print(c,  end=" ")
    print(k)


pattern = "CCAGTCAATG"
d = 1
nei(pattern, d)
