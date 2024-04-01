# =============================================================================
# The following program takes a phrase "Don't panic!"
# Transorms it into a list
# Chnages it into: "on tap"
# Transforms it back into a String
# Prints the new phrase
# Use list methods: pop(), remove(), extend(), insert()
# *****************************************************************************
# Konstanitn Pankratov
# 2024-04-01
# =============================================================================

phrase = "Don't panic!"
plist = list(phrase)

# print String and List before transformation
print("Before transformation:")
print("**********************")
print(phrase)
print(plist)

# =====================================
# Transformation
# =====================================

# remove last 4 characters from the list
for i in range(4):
    plist.pop()

# remopve first character from the list
plist.pop(0)

# remove apostrophe from the list
plist.remove("'")

# Swap the two objects at the end of the list by first popping each object
# from the list, then using the popped objects to extend the list
plist.extend([plist.pop(), plist.pop()])

# pop the space from the list, then insert it back into the list at
# index location 2
plist.insert(2, plist.pop(3))

# transform list into string
new_phrase = ''.join(plist)

# print the results
print("After transformation:")
print("*********************")
print(plist)
print(new_phrase)