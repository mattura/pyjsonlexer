# pyjsonlexer
This lexer takes a JSON-like 'array' string and converts single-quoted array items into escaped double-quoted items,
then puts the 'array' into a python list
Issues such as  ["item 1", '","item 2 including those double quotes":"', "item 3"] are resolved with this lexer
