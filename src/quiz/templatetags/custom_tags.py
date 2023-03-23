from django import template

register = template.Library()


# tag
def expression(value, *args):
    for idx, arg in enumerate(args, 1):
        value = value.replace(f'%{idx}', str(arg))
    return eval(value)


def calculate_progress_correct(a1, a2):
    progress = (a1 / (a1 + a2)) * 100
    return progress


def calculate_progress_incorrect(a1, a2):
    progress = (a2 / (a1 + a2)) * 100
    return progress


# {% expression '(%1 - 1) * 100 // %2' 23 56 as progress_level %}


"""
    '(%1 - 1) * 100 // %2' % (34, 56)  ===>   '(34 - 1) * 100 // 56'
    args = (23, 56)
    1 23
    2 56
    '(23 - 1) * 100 // 56'
"""

register.simple_tag(func=expression, name='expression')
register.simple_tag(func=calculate_progress_correct, name='calculate_progress_correct')
register.simple_tag(func=calculate_progress_incorrect, name='calculate_progress_incorrect')
