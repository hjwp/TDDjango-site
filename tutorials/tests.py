from docutils.core import publish_parts
from django.http import HttpRequest
from django.test import TestCase
from mock import patch
from textwrap import dedent

from tddjango_site.tutorials.views import tutorial


class RSTDirectiveTest(TestCase):

    @patch('tutorials.views.publish_parts')
    def test_tutorial_view_can_handle_filename_sourcecode_rst_directive(self, mock_publish):
        some_rst = dedent('''
            normal string

            header
            ======


            .. sourcecode:: python
                :filename: path/to/filename.py

                    # and some source code
                    foo = lambda x : x + 1

            done
            ''')
        mock_publish.side_effect = lambda _, **k : publish_parts(some_rst, **k)
        response = tutorial(HttpRequest(), '1')
        self.assertNotIn('ERROR', response.content)
        self.assertIn('<h1>header</h1>', response.content)
        self.assertIn('<pre>', response.content)
        self.assertIn('<p class="caption">path/to/filename.py</p>', response.content)


        body_html = publish_parts(some_rst, writer_name='html')['html_body']
        self.assertIn('<h1>header</h1>', body_html)
        self.assertIn('<pre>', body_html)
        self.assertIn('<p class="caption">path/to/filename.py</p>', body_html)
