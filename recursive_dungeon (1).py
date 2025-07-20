import random

def stairs(level: int):
    '''
    a recursive function to print out a set of stairs of varying sizes.
    Achieved by printing one more character per line
    '''
    if level <= 0: #only deal with positive input
        return
    try:
        stairs(level - 1) #recursion
        print('\u2585' * level)
            
    except RecursionError:  #error handling
        print("Error: Maximum recursion depth exceeded")
        return

def square(size: int, current = 0):
    '''
    a recursive function to print out a square
    The top and bottom are implemented by directly printing size characters.
    For the middle part, print characters on both sides and size - 2 spaces in the middle.
    '''
    if size <= 0 or size <= current: #only deal with positive input
        return
        
    try:
        if current < size:
            if current == 0 or current == size - 1:   #print top and bottom
                print('\u25c6' * size)
            else:
                print('\u25c6' + ' ' * (size - 2) + '\u25c6') #print middle rows
            square(size, current + 1)  #recursion, next row

    except RecursionError:  #error handling
        print("Error: Maximum recursion depth exceeded")
    return


def diamond(size: int, row = 0):
    '''
    a recursive function to print out a diamond
    the diamond is a symmetrical figure, 
    so after calculating mid, we can handle it separately using symmetry.
    Since it is a hollow figure, we can draw on the idea of the square.
    top and bottom parts be handled specially.
    '''
    if size <= 0 or size % 2 == 0 or size <= row:    #non-positive or even, line finish printed
        return

    try:
        mid = size // 2 #calculate middle row
        if row <= mid:    #determine current line distance from the middle
            current = row
        else:
            current = size - row - 1
            
        if current > 0: #if the top or bottom
            print(' ' * abs(mid - current) + '*' + ' ' * abs(current * 2 - 1) + '*' + ' ' * abs(mid - current))
        else:   
            print(' ' * mid + '*' + ' ' * mid)
        
        if row < size - 1:  #recursion
            diamond(size, row + 1)

    except RecursionError:  #error handling
        print("Error: Maximum recursion depth exceeded")
        return

def mirror(string: str):
    '''
    a recursive function to reverse any string that is given as an input
    '''
    try:
        if len(string) == 0: #if done
            print()
            return
        print(string[-1], end='')    #print the last character
        mirror(string[:-1])  #recursion, deal with the remaining string without last character

    except RecursionError:  #error handling
        print("Error: Maximum recursion depth exceeded")
        return

#generate random sentences based off a file
def generate_structure(file_path: str):
    '''
    a function to read the sentence structure from a file and represent it in a dict.
    open the file and read it.
    obtain the key and value, store them in a dict by key
    input validation, consider if line is null
    '''
    structure={}
    try:
        with open(file_path, 'r') as file:  #open file
            for line in file:
                line = line.strip()
                if line:    #if this not empty
                    try:
                        key, value = line.split(':')    #get key & value
                        structure[key]=value.split('|') #separate the value and store it
                    except ValueError:
                        print("ValueError")
    except FileNotFoundError:
        print("FileNotFoundError")
    return structure

def generate_sentence(symbol, structure):
    '''
    a recursive function to generate a sentence using that structure.
    randomly select an expr to obtain a list
    if is <>, recursion needs to be continued for processing
    '''
    if symbol not in structure:
        print(f"[unknown {symbol}]", end='')
        return

    expr=random.choice(structure[symbol])   #randomly select an expr
    parts = expr.split(',') #split the expression to get a list
    for part in parts: 
        part = part.strip()
        if part.startswith('<') and part.endswith('>'): #if this a signal that need recursion
            generate_sentence(part, structure)
        else:
            print(part, end=' ')   

def story(encounters: int):
    '''
    a recursive function to create a story that has a number of random encounters
    loop the parameter times, generate random encounter, and then use if
    '''
    if encounters == 0:
        return
    '''
    Placing it at the front is equivalent to continuously recursing without performing operations first, 
    ensuring that the initial statement is generated only once.
    '''
    story(encounters - 1)

    #initial message
    if encounters == 1:
        print("You enter the dungeon...")
    
    #a random encounter
    encounter_type = random.randint(1, 4)
    
    if encounter_type == 1:  #finding stairs
        print("You've found some descending stairs, would you like to go down? ", end='')
        input_str = input().lower()
        if input_str == "yes" or input_str == "y":
            #random number between 1 and 10
            num_stairs = random.randint(1, 10)
            stairs(num_stairs)
        else:
            print("You choose not to go down.")
    
    elif encounter_type == 2:  #finding treasure
        #90% square gem, 10% diamond
        if random.random() < 0.9:  #square gem
            print("You found a square gem!")
            #size between 1 and 5
            gem_size = random.randint(1, 5)
            square(gem_size)
        else:  #diamond
            print("You found a rare diamond!")
            diamond_size = random.randrange(1, 16, 2)  #odd between 1 and 15
            diamond(diamond_size)
    
    elif encounter_type == 3:  #mirror realm
        print("You've found the mirror realm! Anything you say will be reversed, try it out: ", end='')
        user_message = input()
        mirror(user_message)
    
    elif encounter_type == 4:  #mysterious Stranger
        print("You come across a mysterious stranger, he warns you that...")
        try:
            structure = generate_structure("stranger_structure.txt")
            # Generate a sentence starting with <s>
            generate_sentence('<s>', structure)
            print()
        except FileNotFoundError:
            print("FileNotFoundError")

