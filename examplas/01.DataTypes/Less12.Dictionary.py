salary = {"Administration": 8000, "IT": 10000, "Support": 11000, "QA": 14000, "Automation": 18000}
print(type(salary))
print(salary["IT"])
print(salary.get("QA"))

print("~~~~~ List inside Dictionary~~~~")
salary_with_List = {"Support": 11000, "QA": [14000, 10000, 12000, 8000], "Automation": 18000}
print(salary_with_List["QA"])
print(salary_with_List["QA"][3])
print(salary_with_List.get("QA")[0])
print(salary_with_List["QA"].index(10000))


print("~~~~~ Dictionary inside Dictionary~~~~")
emp = {"CEO": "Moshe", "VPRND": "David", "RND": {"QA": "Max", "Dev": "Chaim"}, "DBA": "Shlomo"}
print(emp.get("RND").get("QA"))

#print(emp.get("RND")["DBA"]) - Net!!!!

print("~~~~~ Add Element to Dictionary~~~~")
print(emp)
emp["Team Leader"] = "Yael"
print(emp)

print("~~~~~ Update Element in  Dictionary~~~~")
emp["Team Leader"] = "Idan"
print(emp)

print("~~~~~ Remove Element from  Dictionary~~~~")
emp.pop("Team Leader")
print(emp)

del emp["VPRND"]
print(emp)