#This lexer takes a JSON-like 'array' string and converts single-quoted array items into escaped double-quoted items,
#then puts the 'array' into a python list
#Issues such as  ["item 1", '","item 2 including those double quotes":"', "item 3"] are resolved with this lexer
items = []      #List of lexed items
item = ""       #Current item container
dq = True       #Double-quotes active (False->single quotes active)
bs = 0          #backslash counter
in_item = False #True if currently lexing an item within the quotes (False if outside the quotes; ie comma and whitespace)
for c in stringtoparse[1:-1]:   #Assuming encasement by brackets
    if c=="\\": #if there are backslashes, count them! Odd numbers escape the quotes...
        bs = bs + 1
        continue                    
    if (dq and c=='"') or (not dq and c=="'"):  #quote matched at start/end of an item
        if bs & 1==1:   #if escaped quote, ignore as it must be part of the item
            continue
        else:   #not escaped quote - toggle in_item
            in_item = not in_item
            if item!="":            #if item not empty, we must be at the end
                items += [item]     #so add it to the list of items
                item = ""           #and reset for the next item
            continue                
    if not in_item: #toggle of single/double quotes to enclose items
        if dq and c=="'":
            dq = False
            in_item = True
        elif not dq and c=='"':
            dq = True
            in_item = True
        continue
    if in_item: #character is part of an item, append it to the item
        if not dq and c=='"':           #if we are using single quotes
            item += bs * "\\" + "\""    #escape double quotes for JSON
        else:
            item += bs * "\\" + c
        bs = 0
