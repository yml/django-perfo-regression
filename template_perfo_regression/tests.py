import timeit
from django.utils import unittest
from django.template import RequestContext, loader

class TemplatePerfoTestCase(unittest.TestCase):
    def setUp(self):
        self.params = {'foo': 'bar'}

    def rendered_templates(self):
        tmpl = loader.get_template("base.html")
        ctx = RequestContext({}, self.params)
        return tmpl.render(ctx)


    def test_template_performance(self):
        self.assertEqual(u'btc {0} \n\n'.format(self.params["foo"]),self.rendered_templates())
        timer = timeit.Timer(self.rendered_templates)
        print timer.timeit(1000)
