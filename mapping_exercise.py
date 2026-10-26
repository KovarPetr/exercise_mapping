from math import floor


def brute_force(text, p):
    kmer_len = len(p)
    indices = []
    for kmer_start in range(len(text) - kmer_len + 1):
        if text[kmer_start:kmer_start + kmer_len] == p:
            indices.append(kmer_start)
    return indices

def suffix_array(text):
    list_suff = []
    for i in range(len(text)):
        list_suff.append(text[i:])
    list_suff = [(y, x) for x, y in list(enumerate(list_suff))]
    list_suff.sort()

    return [y for x,y in list_suff]

def find_block(text, sa, p):
    start = [0, len(sa)]
    end = [0, len(sa)]
    while start[0] != start[1] and end[0] != end[1]:
        print(start, end)
        start_mid = floor((start[0] + start[1]) / 2)
        end_mid = floor((end[0] + end[1]) / 2)
        print(start_mid, end_mid)
        if text[sa[start_mid]:sa[start_mid]+len(p)] < p:
            start[0] = start_mid + 1
        else:
            start[1] = start_mid
        if text[sa[end_mid]:sa[end_mid]+len(p)] <= p:
            end[0] = end_mid + 1
        else:
            end[1] = end_mid
    return[start[0], end[1]]

print(suffix_array("CGTACAGTAGTA$"))
print("CGTACAGTAGTA$"[12])
print(find_block("CGTACAGTAGTA$",suffix_array("CGTACAGTAGTA$"), "GTA"))


