from django import template

register = template.Library()


def update_variable(value, arg):
    data = value*arg
    value = data
    return value


# Method 2 for queryset or python List
def intersection(queryset1, queryset2):
    return list(set.intersection(set(queryset1), set(queryset2)))


register.filter('intersection', intersection)


register.filter('update_variable', update_variable)
