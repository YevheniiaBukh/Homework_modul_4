

def get_cats_info(path):
    try:
        with open(path, 'r')as file:
            cats_info = []
            for line in file:
                line = line.strip()
                parts = line.split(',')
                cat = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats_info.append(cat) 
        return cats_info
    except FileNotFoundError:
        print('Not found cat')
        
cats_info = get_cats_info("cats.txt")
print(cats_info)


                
        