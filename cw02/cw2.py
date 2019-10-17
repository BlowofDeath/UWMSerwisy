lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'

lorem = '{:.40}'.format(lorem)

print(lorem)



lorem1 = '{:.10}'.format(lorem)
lorem2 = '{:.12}'.format(lorem)
print(lorem1)
print(lorem2)



lorem = '{:{align}{width}}'.format(lorem, align='^', width='90')

print(lorem)