# coding=utf-8

# Measurements
measurements_dict = {
    0: {
        'measurement': 'edge',
        'unit': 'bool'
    }
}

# Input information
INPUT_INFORMATION = {
    'input_name_unique': 'RPI_EDGE',
    'input_manufacturer': 'Raspberry Pi',
    'input_name': 'RPi Edge',
    'measurements_name': 'Rising/Falling Edge',
    'measurements_dict': measurements_dict,

    'options_enabled': [
        'gpio_location',
        'period',
        'pre_output'
    ],
    'options_disabled': ['interface'],

    'dependencies_module': [
        ('apt', 'gcc', 'gcc'),
        ('pip-pypi', 'RPi.GPIO', 'RPi.GPIO')
    ],

    'interfaces': ['GPIO']
}
