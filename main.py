from tkinter import *
window = Tk()
window.geometry('500x300')
window.title('Minecraft Item Chooser')
instructions = StringVar(value='Item name')
Label(window, textvariable=instructions).pack()
instructions_input = StringVar()
Entry(window, textvariable=instructions_input).pack()
item = ''
unbreakable = False
enchantments = []
def normalize(id):
	return id.lower().replace(' ', '_')
def add_enchantment():
	enchantment_name = input('Name: ')
	enchantment_level = input('Level: ')
	enchantments.append((normalize(enchantment_name), enchantment_level))
	if input('More enchantments? (y/n): ') == 'y':
		add_enchantment()
def resetInput():
	instructions_input.set('')
def setCompletion(completion):
	window.bind('<Return>', completion)
def setItem(event):
	item = instructions_input.get()
setCompletion(setItem)
def setUnbreakable(event):
	unbreakable = instructions_input.get()
instructions.set('Unbreakable? (y/n)')
setCompletion(setUnbreakable)
window.mainloop()




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
print(attributes + '\nCopied to clipboard')
pyperclip.copy(attributes[1:])