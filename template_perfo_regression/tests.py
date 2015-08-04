import timeit
from django.utils import unittest
from django.template import RequestContext, loader

class TemplatePerfoTestCase(unittest.TestCase):
    def setUp(self):
        self.params = {'foo': 'bar', 'range': range(10)}

    def rendered_templates(self):
        tmpl = loader.get_template("base.html")
        ctx = RequestContext({}, self.params)
        return tmpl.render(ctx)


    def test_template_performance(self):
        timer = timeit.Timer(self.rendered_templates)
        print timer.timeit(1000)
