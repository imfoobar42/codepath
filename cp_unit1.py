def final_value_after_operations(operations):
    count =1
    for operation in operations:
        if operation == "bouncy" or operation=="flouncy":
             count += 1
        elif operation=="trouncy" or operation=="flouncy":
              count -=1
        else:
            raise Exception('Error in input')        
    return count

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))


def tiggerfy(word):
  set={'t','T','i','I','gg','GG','er','ER'}
  result = word
  for i in set:
    result = result.replace(i,'')
  return result

print(tiggerfy('Trigger'))
print(tiggerfy('eggplant'))
print(tiggerfy('Choir'))


def non_decreasing(nums):
  for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
      return False
  return True
        
     
def reverse_sentence(sentence):
    #splits
    sentence_split= sentence.split()
    #['tubby','little','yoyo']
    reverse_sentence = sentence_split[::-1]
    join_sentence = ' '.join(reverse_sentence)
    return join_sentence

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)  

def goldilocks_approved(nums):
    if len(nums)<3: 
      return -1
    minNums = min(nums)
    maxNums = max(nums)
    for num in nums:
       if num != minNums and num!=maxNums:
          return num
    return -1


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))


def delete_minimum_elements(hunny_jar_sizes):
	return sorted(hunny_jar_sizes)




hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

def sum_of_digits(num):
    sum = 0
    while(num>0):
      rem =num % 10
      sum += rem
        #print(f'num: {num}, sum:{sum}')
      num = num//10
    return sum

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))

