from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


# https://stackoverflow.com/a/2180209/4494547
def usd(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])


register.filter('usd', usd)
