### **Day Three: *lists, dictionaries, and indexing***

# Dot's new rural abode is in a bit of disrepair. It desperately needs some care before it can be the cozy hide-away they've been dreaming of. The paint on the walls is dull and peeling, and some of the floorboards have rotted away.
# The previous occupants were beginning to tackle the repairs before they moved out. They left Dot a shopping list for what's needed to complete the repairs. However, Dot is really particular with how they want the place to look. They want to change the shopping list so that it reflects the changes they want to make to the house.

### Challenge
'''
Dot has some specific rules for what they want to change in the shopping list: 

1. They hate oak wood, and prefer maple.
2. They want to paint all the rooms blue except the kitchen, which they want to paint white. 

```
old_blueprint = {
    "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],
    "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],
    "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],
    "Bedroom" : ["Clean", 'Mahogany', 'Good Condition', 'Green'],
    "Bathroom": ["Dirty", 'White Tile', 'Good Condition','White'],
    "Shed"    : ['Dirty', "Cherry", "Damaged", "Un-painted"]
}

shopping_list = ['20 x Oak Plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']
```

**Note:** The blueprint above is in a dictionary format and we won't be needing to work with dictionaries in the challenge, use the blueprint as reference only. 

**Use python's pop(), insert(), and append() list functions to change the shopping_list above so that it reflects the right materials needed.**

The list should be ordered by wood types first, then paint types.

```
example_shopping_list = ['wood type in room A', 'wood type in room b','paint type in room a','paint type in room b']
```

**Create a paint_list list from the new_shopping_list list using the built in python list indexing ability.**
'''

#shopping list 
new_shopping_list = ['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']
# ANSWER 
paint_list = new_shopping_list[3:]