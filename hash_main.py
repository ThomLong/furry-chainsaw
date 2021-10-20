import HashSet as hset

# Program starts

# Initialize word set
words = hset.HashSet()   # Create new empty HashSet
words.init()             # Initialize with eight empty buckets

# Add names to word set. Notice: a) contains duplicate names,
# b) more than eight names ==> will trigger rehash
names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Jonas", "Amer", "David"]
for name in names:
    words.add(name)

print("\nto_string():", words.to_string())  # { Adam David Amer Ceve Owen Ella Jonas Morgan Fredrik Zoe Fred Albin Ola Simon }
print("get_size():", words.get_size())             # 14
print("contains(Fred):", words.contains("Fred"))   # True
print("contains(Bob):", words.contains("Bob"))     # False

# Hash specific data
mx = words.max_bucket_size()
print("\nmax bucket:", mx)                # 2
buckets = words.bucket_list_size()
print("bucket list size:", buckets)     # 16

# Remove elements
delete = ["Ceve", "Adam", "Ceve", "Jonas", "Ola"]
for s in delete:
    words.remove(s)
print("\nget_size:", words.get_size())   # 10
print("to_string():", words.to_string())   # { David Amer Owen Ella Morgan Fredrik Zoe Fred Albin Simon }
