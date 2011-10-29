from docutils.core import publish_string
from django.shortcuts import render
from django.utils.safestring import mark_safe
import os
import rst_directive
ROOT = os.path.split(os.path.dirname(__file__))[0]

PAGE_NUMBERS = [1, 2, 3]

def tutorial(request, number=1):
    number = int(number)
    rst_file = os.path.join(ROOT, 'rst', 'tutorial%02d.rst' % number)
    with open(rst_file) as f:
        rst_contents = mark_safe(publish_string(f.read(), writer_name='html'))
    return render(request, 'tutorial.html', dict(
        rst_contents=rst_contents,
        page_number=number,
        page_numbers=PAGE_NUMBERS,
    ))

