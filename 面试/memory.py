variable6 = ['new']
print('Variable6: ', variable6)


def update_variable(variable_to_update):
    # variable_to_update.append('inside')
    variable_to_update = 'var1'
    print(f'inner:{id(variable_to_update)}')
    print(variable_to_update)


update_variable(variable6)
print('Variable6: ', variable6)
print(f'outer:{id(variable6)}')

print('-' * 20)

variable_nine = "a" * 5000
variable_ten = "a" * 5000
print('Variable9: ', id(variable_nine))
print('Variable10: ', id(variable_ten))
