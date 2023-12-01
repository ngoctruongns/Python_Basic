def simple_generator():
    yield 1
    yield 2
    yield 3

# Sử dụng generator
gen = simple_generator()

# print(next(gen))  # In ra: 1
# print(next(gen))  # In ra: 2
# print(next(gen))  # In ra: 3
# print(gen.send())

for num in gen:
    print(num)

