ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# change list
ft_list[1] = "World!"

#change tuple
temp_list = list(ft_tuple)
temp_list[1] = "Brazil"
ft_tuple = tuple(temp_list)

#change set
new_value = {"Hello", "São Paulo!"}
ft_set.update(new_value)

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)