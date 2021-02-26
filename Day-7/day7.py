#example dicitonary
user_boxes = {'weight': [4,2,18,21,14,13],
              'box_name': ['box1','box2', 'box3', 'box4', 'box5', 'box6']
             }
def sort_boxes(): 
    weights = user_boxes.get('weight')
    box_names = user_boxes.get('box_name')
    box_maps = dict(zip(weights, box_names))
    for i in sorted(box_maps):
        print(box_maps[i])
    
sort_boxes()

