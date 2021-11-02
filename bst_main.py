# from dataclasses import dataclass
import BstMap as bst

# Program starts
# Add pairs
d = {"Ella": 39, "Owen": 40, "Fred": 44, "Zoe": 41, "Adam": 27, "Ceve": 37}
map = bst.BstMap()
for k, v in d.items():
    map.put(k, v)
# { (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
print(map.to_string())
print("Size:", map.size())    # 6

# Override existing values
print("\nOverride existing values")
map.put("Zoe", 99)
map.put("Ceve", 100)
# { (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }
print(map.to_string())

# get
print("\nGet(Fred):", map.get("Fred"))    # 44
print("Get(Jonas):", map.get("Jonas"))  # None
print("Max depth:", map.max_depth())     # 3

# Check max_depth
map.put("AA", 1)
map.put("AAA", 2)
map.put("AAAA", 3)
map.put("AAAAA", 4)

print("\nSize:", map.size())              # 10
print("Max depth:", map.max_depth())    # 6
# { (AA,1) (AAA,2) (AAAA,3) (AAAAA,4) (Adam,27)
# (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }
print("To_string: ", map.to_string())

# as_list
lst = map.as_list()
print("\nList size and element type:", len(
    lst), type(lst[0]))  # 10 <class 'tuple'>
# [('AA', 1), ('AAA', 2), ('AAAA', 3), ('AAAAA', 4)
# ('Adam', 27), ('Ceve', 100), ('Ella', 39), ('Fred', 44)
# ('Owen', 40), ('Zoe', 99)]
print("List content:", lst)
