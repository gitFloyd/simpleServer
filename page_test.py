from simpleUtility import dump


print("<main><p>This is a test page.<br>It was generated by page_test.py</p>")

list1 = [1,2,3]
set1 = {4,5,6}
tuple1 = (7,8,9)

dic1 = {
	'list': list1,
	'set': set1,
	'tuple': tuple1,
	'fun': (list1, set1, tuple1)
}

dump(dic1)




print("</main>")