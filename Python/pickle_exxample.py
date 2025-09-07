import pickle

my_dict = {
    "name": "Moo",
    "age": 20,
    "job": "developer"
}

# save python object to .pickle file
# with open("saved.pickle", "wb") as stream:
#     pickle.dump(my_dict, stream)

# load pickle file to python object
with open("saved.pickle", "rb") as stream:
     new_dict = pickle.load(stream)
     print(new_dict)