from docutils.core import publish_string
from django.shortcuts import render
from django.utils.safestring import mark_safe
PAGE_NUMBERS = [1, 2, 3]

def tutorial(request, number=1):
    number = int(number)
    with open('rst/tutorial%02d.rst' % number) as f:
        rst_contents = mark_safe(publish_string(f.read(), writer_name='html'))
    return render(request, 'tutorial.html', dict(
        rst_contents=rst_contents,
        page_number=number,
        page_numbers=PAGE_NUMBERS,
    ))

