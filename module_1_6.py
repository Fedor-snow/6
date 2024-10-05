my_dict = {"Ivan" : 1986, "Igor" : 1999}
print(my_dict)
print(my_dict. get("Ivan"))
my_dict. update({"Anna" : 2010, "John" : 2000})
print(my_dict)
a = my_dict. pop("Ivan")
print(a)
print(my_dict)

my_set = {1, 2, 3, 4, 4, 4, 2, 3, 1, "Text", False }
print(my_set)
my_set. add(5)
my_set. add(6)
my_set. discard("Text")
print(my_set)