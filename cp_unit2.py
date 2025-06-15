#Dictionaries

#P1
def lineup(artists, set_times):
  return (dict(zip(artists,set_times)))


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

#print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))


#P2 
def get_artist_info(artist, festival_schedule):
  if artist in festival_schedule:
    return festival_schedule[artist]
  else:
    return {'message':'Artist not found'}
  
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

#print(get_artist_info("Blood Orange", festival_schedule)) 
#print(get_artist_info("Taylor Swift", festival_schedule))  

#P3 Ticket Sales

def total_sales(ticket_sales):
    return sum(ticket_sales.values()) #dict.values() returns a list of values

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
#print(total_sales(ticket_sales))

#tuple can be key as it is immutable 
#P4
#items return tuples of [(key,value)]  
def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}
    for artist,time in venue1_schedule.items():
      if artist in venue2_schedule:
         if venue2_schedule[artist]== time:
            result[artist]=time
    return result   

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

#print(identify_conflicts(venue1_schedule, venue2_schedule))

#def get_winner(votes):
#    pass



def total_sales(ticket_sales):
  return sum(ticket_sales.values())

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

#print(total_sales(ticket_sales))

def identify_conflicts(venue1_schedule, venue2_schedule):
  conflict = {}
  for artist in venue1_schedule.keys():
    if artist in venue2_schedule and venue1_schedule[artist]== venue2_schedule[artist]:
      conflict[artist]= venue2_schedule[artist]
  return conflict

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

#print(identify_conflicts(venue1_schedule, venue2_schedule))

#P5 
#Frequency map of artist:vote count 
from collections import Counter

def best_set(votes):
    res = Counter(votes.values()) #sza -1 ,...
    maxCount =0
    for artist,vote in res.items():
      if(vote)> maxCount:
        maxCount = vote
        winner = artist
    return winner

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1278: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "Ethel Cain"
}

#print(best_set(votes1))
#print(best_set(votes2))

#P6
def max_audience_performances(audiences):
  maxAudience = max(audiences)
  return Counter(audiences)[maxAudience]* maxAudience # 100 -2 , 200 -3 
  #return res[maxAudience]*maxAudience


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

#print(max_audience_performances(audiences1))
#print(max_audience_performances(audiences2))

#P8
def num_popular_pairs(popularity_scores):
  
    res = Counter(popularity_scores) #frequency map
    totalPairs = 0
    for n in res.values():
      if n >= 2: 
        totalPairs += n*(n-1)//2
    return totalPairs
  
popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 
    
    
#P9
def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    indexS = {performer : index for index,performer in enumerate(s)}
    totalDiff = 0
    for index, performer in enumerate(t):
      totalDiff +=abs(indexS[performer]- index)
    return totalDiff

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

#print(find_stage_arrangement_difference(s1, t1))
#print(find_stage_arrangement_difference(s2, t2))

#P10

def num_VIP_guests(vip_passes, guests):
    vipSet = set(vip_passes)
    return sum(1 for c in guests if c in vipSet)

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))
  