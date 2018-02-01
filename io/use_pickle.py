import pickle

d = dict(name='bob', age=18, score=90)
print(d)

data = pickle._dumps(d)

print(data)

reborn = pickle.loads(data)
print(reborn)