rew_tags = [
    'Python', 'django', 'PYHTON', '   ', 'FastAPI', 'django ', 'Machine Learning', 'python', ''
]

tags_clear = []
for tag in rew_tags:
    texto = tag.strip().lower()
    if texto != '':
        tags_clear.append(texto)

resultado = set(tags_clear)
print(resultado)