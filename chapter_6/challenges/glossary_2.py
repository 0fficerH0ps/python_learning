# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. 

# When you’re sure that your loop works, add five more Python terms to your
# glossary.

# When you run your program again, these new words and meanings should
# automatically be included in the output.


glossary = {'dictionary': 'a place to keep a whole bunch of information.',
			'newline character': 'a back slash and the letter n use: jump to next line',
			'get() method': 'set a default value that will be returned if the requested key doesn’t exist.',
			'traceback': 'results showing a KeyError',
			'tab space': 'the amount of spaces a tab is set to equal, ie. 4'}

for term, definition in glossary.items():
	print(f"{term.title()}:\n\t{definition}")

glossary['print'] = 'command use to exicute code...ish'
glossary['del'] = 'command used to perminately remove item'
glossary['key-value'] = 'just that, key values in a dictionary'
glossary['key'] = 'the first item in a python dictionary pair'
glossary['value'] = 'the second item in a python dictionary pair'

for term, definition in glossary.items():
	print(f"{term.title()}:\n\t{definition}")
