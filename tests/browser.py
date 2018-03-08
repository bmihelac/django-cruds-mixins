"""
Updated from http://djangosnippets.org/snippets/2321/
"""
import os, tempfile, subprocess


URL_OPENER = 'open'


def display(content):
    """ Saves a response's content to a temporary file and opens it in a
    browser.
    ::

        from impckg.utils.test.browser import display; display(response.content)
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
    temp_file.write(content)
    dev_null = open(os.devnull, 'w')
    kwargs = {'stdout': dev_null, 'stderr': dev_null}
    subprocess.Popen([URL_OPENER, temp_file.name], **kwargs)

