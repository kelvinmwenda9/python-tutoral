employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]


dict = {i["id"]:i['name'][0] for i in employee_list}
print(dict)

# print(employee_list)

def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

# print(mod(employee_list))

def to_mod_list(employee_list):
   """ Modifies the employee list of dictionaries into list of employee-department strings

   [IMPLEMENT ME] 
      1. Use the map() method to apply mod() to all elements in employee_list

   Args:
      employee_list: list of employee objects

   Returns:
      list - A list of strings consisting of name + department.
   """
   ### WRITE SOLUTION CODE HERE
   map_emp = map(mod, employee_list)   
   list = []

   for x in map_emp:
    list.append(x)
  
   return list

# print(to_mod_list(employee_list))

mod_list = to_mod_list(employee_list)
# print(list[1])

# map_e = to_mod_list(employee_list)

# for e in map_e:
#     print(e)


def generate_usernames(mod_list):
   """ Generates a list of usernames 

   [IMPLEMENT ME] 
      1. Use list comprehension and the replace() function to replace space
         characters with underscores

      List comprehension looks like:
      list = [ function() for <item> in <list> ]

      The format for the replace() function is:

      test_str.replace(“a”, “z”) # replaces every “a” in test_str with “z”

   Args:
      mod_list: list of employee-department strings

   Returns:
      list - A list of usernames consisting of name + department delimited by underscores.
   """
   ### WRITE SOLUTION CODE HERE
   list = [i.replace(" ", "_") for i in mod_list]

   return list


print(generate_usernames(mod_list))



numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)