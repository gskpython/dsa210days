thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # "cherry", "orange", "kiwi"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # "apple", "banana", "cherry", "orange"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # "cherry", "orange", "kiwi", "melon", "mango"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # "orange", "kiwi", "melon",

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"  # overwites 2nd element
print(thislist) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #overwites banana and cherry 
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # second one is replaced with two new values
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # change banana and cherry and insert watermelon
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # inserts watermelon as third
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")  # can add any iterable
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # removes second element
print(thislist) 

thislist = ["apple", "banana", "cherry"]
del thislist[0] # deletes apple
print(thislist) 

thislist = ["apple", "banana", "cherry"]
del thislist # deletes the entire list

thislist = ["apple", "banana", "cherry"]
thislist.clear() #clears 
print(thislist)