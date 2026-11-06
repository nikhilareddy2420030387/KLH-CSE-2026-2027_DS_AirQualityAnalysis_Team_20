def jaccard_index(str1, str2):
    set1, set2 = set(str1.split()),set(str2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

#example usage
s1 ="data science is fun"
s2 = "science makes data useful"

print("jaccard Index:", jaccard_index(s1,s2))