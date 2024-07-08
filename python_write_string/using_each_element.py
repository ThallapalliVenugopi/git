x = 'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. ' \
    'Its high-level built in data structures, combined with dynamic typing and dynamic binding, make ' \
    'it very attractive for Rapid Application Development, as well ' \
    'as for use as c scripting or glue language to connect existing components together.' \
    ' Pythons simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.' \
    ' Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and ' \
    'the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. '
w=x.split()

d = dict()
for i in w:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

