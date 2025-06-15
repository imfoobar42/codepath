#Advanced Problem V1 
from collections import Counter 
#P1 
def find_balanced_subsequence(art_pieces):
  freqMap = Counter(art_pieces)
  maxLen = 0
  for x in art_pieces:
     if x+1 in freqMap:
       currentLen = freqMap[x+1] + freqMap[x]
       maxLen = max(currentLen,maxLen)
  return maxLen
  
art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))


# #P2
# def is_authentic_collection(art_pieces):
#     if max(art_pieces)>len(art_pieces):
#       return False
#     freqMap = Counter(art_pieces)
#     for x in range(1,)

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))   



#P3 
def organize_exhibition(collection):
    freqMap = Counter(collection)
    result =[]
    keys = list(freqMap.keys()) #list
    while freqMap:
      row = []
      for k in keys:
        row.append(k)
        if freqMap[k]==1:
          del freqMap[k]
          keys.remove(k)
        else:
          freqMap[k] -=1
      result.append(row)
    return result

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2)) 


#P4
#
#    word.com