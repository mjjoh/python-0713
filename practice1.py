my_dict = {
	"key1": 1,
	"key3": 2,
	"key2": 3
}
print(my_dict.items())

#list comprehension
#[(추가할 요소의 도출 식) for (변수이름) in (Iterable Data Type)]
my_list = [abc[0] for abc in ['abc', 'bcd', 'cde']]
print(my_list)

list1 = [(i,j) for i in range(0,3) for j in range(0,3)]
print(list1)

def my_func(param1):
	param1 *= 2
	return param1
asd=my_func(3)
print(asd)

def without_return(param1):
    return str(param1) * 2
ref=without_return(10)
print(ref)

def my_funct(num):
    return num ** 3
	
print(my_funct(4))

def get_input_and_format():
	user_input = input("Type something: ")
	if user_input.isdigit():
		user_input = int(user_input)
	else:
		user_input = user_input.lower()
	return user_input

input1 = get_input_and_format()
input2 = get_input_and_format()
print(input1, input2)


b = lambda x, y : x+y
print(b(1,2))
#print(b(1, 2))
#my_dict = {'key1': 1, 'key2': 3, 'key3': 2}
#lst=list(my_dict.items())
#print(lst)
#sorted(my_dict.items(), key=lambda x: x[1])
#print(my_dict)
print(range(2))