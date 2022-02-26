
tabchar = '&nbsp;&nbsp;&nbsp;'
newlinechar = '<br>'
if __name__ == '__main__':
	tabchar = '   '
	newlinechar = '\n'


def _dump(var, depth = 0, prefix = ''):
	tab = ''.join([tabchar for num in range(0,depth)])
	typename = type(var).__name__
	if typename == 'int' or typename == 'str':
		return tab + prefix + str(var) + newlinechar
	elif typename == 'list' or typename == 'tuple' or typename == 'set':
		brace = '['
		endbrace = ']'
		if typename == 'tuple':
			brace = '('
			endbrace = ')'
		elif typename == 'set':
			brace = '{'
			endbrace = '}'
		output = tab + prefix + brace + newlinechar
		output += ''.join([_dump(value, depth+1) for value in var])
		output += tab +endbrace + newlinechar
		return output
	elif typename == 'dict':
		output = tab + prefix + '{' + newlinechar
		output += ''.join([_dump(var[key], depth+1, key + ': ') for key in var.keys()])
		output += tab + '}' + newlinechar
		return output

def dump(var):
	print(_dump(var), newlinechar)
