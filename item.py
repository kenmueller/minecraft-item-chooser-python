import pyperclip
def normalize(id):
	return id.lower().replace(' ', '_')
def add_enchantment():
	enchantment_name = input('Name: ')
	enchantment_level = int(input('Level: '))
	enchantments.append((normalize(enchantment_name), str(min(enchantment_level, 32767))))
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
		attributes += 'Unbreakable:1'
	if not enchantments_is_empty:
		attributes += (',' if unbreakable else '') + 'Enchantments:[' + ','.join(['{id:' + enchantment[0] + ',lvl:' + enchantment[1] + '}' for enchantment in enchantments]) + ']'
	attributes += '}'
print('Copied to clipboard\n\n' + attributes + '\n')
pyperclip.copy(attributes[1:])