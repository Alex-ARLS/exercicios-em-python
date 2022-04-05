vogais_ ={'aeiou'} # sem o construtor
print(type(vogais_), vogais_)
vogais_1 = set('aeiouuuoiuioeaaa')# construtor com string
print(type(vogais_1), vogais_1)
vogais_2 = set(['a','e','i','o','u'])# construtor com lista
print(type(vogais_2),vogais_2)
vogais_3 = set(('a','e','i','o','u'))#construtor com tupla
print(type(vogais_3),vogais_3)

print (set('cafe'))