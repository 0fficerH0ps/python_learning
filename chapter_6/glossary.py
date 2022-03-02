# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
#   chapters. Use these words as the keys in your glossary, and store their
#   meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
#   print the word followed by a colon and then its meaning, or print the word
#   on one line and then print its meaning indented on a second line. Use the
#   newline character (\n) to insert a blank line between each word-meaning
#   pair in your output.

glossary = {'dictionary': 'a place to keep a whole bunch of information.',
			'newline character': 'a back slash and the letter n use: jump to next line',
			'get() method': 'set a default value that will be returned if the requested key doesn’t exist.',
			'traceback': 'results showing a KeyError',
			'tab space': 'the amount of spaces a tab is set to equal, ie. 4'}
print(f"Dictionary:\n    {glossary['dictionary']}")
print(f"Newline Character:\n    {glossary['newline character']}")
print(f"Get() Method:\n    {glossary['get() method']}")
print(f"Traceback:\n    {glossary['traceback']}")
print(f"Tab Space:\n    {glossary['tab space']}")
