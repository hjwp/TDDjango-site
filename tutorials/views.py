from docutils.core import publish_parts
import os

from docutils.parsers.rst import directives
from django.shortcuts import render
from django.utils.safestring import mark_safe
from tddjango_site.tutorials.rst_directive import PygmentsWithFilenameCaption

ROOT = os.path.split(os.path.dirname(__file__))[0]
PAGE_NUMBERS = [1, 2, 3, 4, 5]

def tutorial(request, number=None):
    directives.register_directive('sourcecode', PygmentsWithFilenameCaption)
    if number is None:
        rst_file = os.path.join(ROOT, 'source', 'README.rst')
    else:
        number = int(number)
        rst_file = os.path.join(ROOT, 'source', 'tutorial%02d.rst' % number)
    with open(rst_file) as f:
        html_parts = publish_parts(f.read(), writer_name='html')
        rst_contents = mark_safe(html_parts['html_body'])
    return render(request, 'tutorial.html', dict(
        rst_contents=rst_contents,
        page_number=number,
        page_numbers=PAGE_NUMBERS,
    ))

