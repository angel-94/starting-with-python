
demo_list = [1, 'dos', True]

print(f"Lista values is -- {demo_list}")

colors = ['Yellow', 'Green', 'Red']
print(colors)


# utilizando una tupla para crear una lista
new_list = list((1, 2, 3))
print(new_list)


# Create a list whit range
list_range = list(range(1, 10))
print(list_range)

data_type_colors = type(colors)
print(data_type_colors)

# Imprimimos los métodos y atributos con dir
# print(dir(colors))

print(f"lONGITUD DE COLORES --> {len(colors)}")
print(colors[-2])


print(f"Esta el color dentro de la lista ---> {'Red' in colors}")
print(f"Esta el color dentro de la lista ---> {'Otro color' in colors}")

print(colors)
colors[1] = "Blue"
print(colors)

colors.append(list(('violet', 'Otro color')))
colors.extend(['Color1', 'color2'])


print(colors)

new_colors = ['colo1', 'color2']
new_colors.insert(-1, 'Violet')
new_colors.insert(len(new_colors), 'Violet 22')
print(new_colors)
# new_colors.pop()
# new_colors.pop()
print(new_colors)
# new_colors.remove('colo1')
# new_colors.pop(0)
new_colors.sort(reverse=True)
print(new_colors)


# Obtener indice
print(new_colors.index('colo1'))







