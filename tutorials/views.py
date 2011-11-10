from docutils.core import publish_string
import rst_directive #needed for docutils publish to do python syntax highlighting
import os

from django.shortcuts import render
from django.utils.safestring import mark_safe
ROOT = os.path.split(os.path.dirname(__file__))[0]

PAGE_NUMBERS = [1, 2, 3, 4]

def tutorial(request, number=None):
    if number is None:
        rst_file = os.path.join(ROOT, 'source', 'README.rst')
    else:
        number = int(number)
        rst_file = os.path.join(ROOT, 'source', 'tutorial%02d.rst' % number)
    with open(rst_file) as f:
        rst_contents = mark_safe(publish_string(f.read(), writer_name='html'))
    return render(request, 'tutorial.html', dict(
        rst_contents=rst_contents,
        page_number=number,
        page_numbers=PAGE_NUMBERS,
    ))

