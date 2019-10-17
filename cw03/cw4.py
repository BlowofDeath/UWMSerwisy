def temptype(value, temperature_type='Fahrenheit'):
    if temperature_type == 'Fahrenheit':
        return 1.8 * value + 32
    elif temperature_type == 'Rankine':
        return 0
    elif temperature_type == 'Kelvin':
        return 0
    else:
        print('Błędny typ temperatury')

