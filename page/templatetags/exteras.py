from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

months = {'01': 'فروردین',
          '02': 'اردیبهشت',
          '03': 'خرداد',
          '04': 'تیر',
          '05': 'مرداد',
          '06': 'شهریور',
          '07': 'مهر',
          '08': 'آبان',
          '09': 'آذر',
          '10': 'دی',
          '11': 'بهمن',
          '12': 'اسفند'
          }

days = {'Saturday': 'شنبه',
        'Sunday': 'یکشنبه',
        'Monday': 'دوشنبه',
        'Tuesday': 'سه شنبه',
        'Wednesday': 'چهارشنبه',
        'Thursday': 'پنجشنبه',
        'Friday': 'جمعه'
        }

@register.filter
def datefarsi(value):
    parts = str(value).split(sep=' ')
    if parts[0] == '':
        return ''
    if parts[0][0] == '0':
        parts[0] = parts[0][1]
    parts[1] = months[parts[1]]
    res = " ".join(parts)
    return res


@register.filter
def datetimefarsi(value):
    parts = str(value).split(sep=' ')
    # if parts[0] == '':
    #     return ''
    # if parts[0] in days.keys():
    #     parts[0] = days[parts[0]]
    # if parts[1][0] == '0':
    #     parts[1] = parts[1][1]
    # parts[2] = months[parts[2]]
    # res = parts[0] + " - "
    # res += " ".join(parts[1: 4])
    # res += " ساعت " + parts[-1]
    # return res
    for part in parts:
        print(part)
    res = parts[0]+' '+parts[1]+' - '+parts[2]+' '+months[parts[3]]+' '+parts[4]+' '+'ساعت '+ parts[5]
    return res
