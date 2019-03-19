import pyperclip
def normalize(id):
	return id.lower().replace(' ', '_')
def add_enchantment():
	enchantment_name = input('Name: ')
	enchantment_level = input('Level: ')
	enchantments.append((normalize(enchantment_name), enchantment_level))
	if input('More enchantments? (y/n): ') == 'y':
		add_enchantment()
item = input('Item: ')
unbreakable = input('Unbreakable? (y/n): ') == 'y'
enchantments = []
if input('Add enchantments? (y/n): ') == 'y':
	add_enchantment()
enchantments_is_empty = len(enchantments) == 0
attributes = '/give @p ' + normalize(item)
if unbreakable or not enchantments_is_empty:
	attributes += '{'
	if unbreakable:
		attributes += 'unbreakable:1'
	if not enchantments_is_empty:
		attributes += ',' if unbreakable else '' + 'enchantments:[' + ','.join(['{id:' + enchantment[0] + ',lvl:' + enchantment[1] + '}' for enchantment in enchantments]) + ']'
	attributes += '}'
print(attributes + '\nCopied to clipboard')
pyperclip.copy(attributes)