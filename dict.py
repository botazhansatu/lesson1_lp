

dict2={"city": "Москва", "temperature": "20"}
print(dict2["city"])
dict2["temperature"]=str(int(dict2["temperature"])-5)
print(dict2)
print(dict2.get("country"))
print(dict2.get("country","Russia"))
print(dict2)
dict2["date"]="27.05.2019"
print(dict2)
print(len(dict2))






