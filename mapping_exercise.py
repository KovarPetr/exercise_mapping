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
        start_mid = floor((start[0] + start[1]) / 2)
        end_mid = floor((end[0] + end[1]) / 2)
        if text[sa[start_mid]:sa[start_mid]+len(p)] < p:
            start[0] = start_mid + 1
        else:
            start[1] = start_mid
        if text[sa[end_mid]:sa[end_mid]+len(p)] <= p:
            end[0] = end_mid + 1
        else:
            end[1] = end_mid
    return[start[0], end[1]]




def bwt(text, sa):
    out = ""
    for indx in sa:
        if indx == 0:
            out += text[-1]
        else:
            out += text[indx - 1]
    return out

def first_occurrence(letters):
    out_dict = {}
    let_sort = ''.join(sorted(letters))
    for letter_indx in range(len(let_sort)):
        if let_sort[letter_indx] not in out_dict.keys():
            out_dict[let_sort[letter_indx]] = letter_indx
    return out_dict

def inverse_bwt(bwt):
    f_o = first_occurrence(bwt)
    found = {}
    list_k = []
    for letter in bwt:
        if letter in found.keys():
            found[letter] += 1
            list_k.append(found[letter])
        else:
            found[letter] = 1
            list_k.append(found[letter])
    row = 0
    seq = ""
    for i in range(len(bwt) - 1):
        letter = bwt[row]
        k = list_k[row]
        next_row = f_o[letter] + k - 1
        seq += letter
        row = next_row
    seq = seq[::-1] + "$"

    return seq

print(inverse_bwt("AC$ATGGGGACTC"))
