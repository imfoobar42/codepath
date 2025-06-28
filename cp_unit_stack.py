def manage_stage_changes(changes):
    stack = []
    result = []
    for change in changes:
      
      if "Schedule" in change.split():
        stack.append(change.split()[1])
      elif change== "Cancel":
        last_item = stack.pop()
      else:
        stack.append(last_item)
    return stack   
        

#print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
#print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
#print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

#P2 
#fifo 
#higher >>

from collections import deque  
def process_performance_requests(requests):
    sorted_res = sorted(requests, reverse=True)
    result = []
    for res in sorted_res:
      result.append(res[1])
    return result  
      #my new item < > add it in front or at the 

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# q =deque(requests)
# sorted(q,reverse=True)
# q.pop()

def collect_festival_points(points):
    stack = []
    sum = 0
    for point in points:
      sum += point
      stack.append(point)
    return sum 


print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 
