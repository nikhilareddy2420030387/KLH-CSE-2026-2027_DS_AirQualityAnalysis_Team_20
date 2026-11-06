def hamming_distance(str1,str2):
    #two strings should be equal
    if len(str1) !=len(str2):
        raise ValueError("Strigs must be of equal length")

    #count differing positions
    return sum(ch1!=ch2 for ch1, ch2 in zip(str1,str2))

#example usage
s1 = "karolin"
s2 = "kathrin"
dist = hamming_distance(s1,s2)
print(f"Hamming Distance between '{s1}' and '{s2}':{dist}")