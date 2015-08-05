import timeit
from django.test import TestCase
from django.template import RequestContext, loader

class TemplatePerfoTestCase(TestCase):
    def setUp(self):
        self.params = {'foo': 'bar', 'range': range(10)}

    def rendered_template(self, template_name):
        tmpl = loader.get_template(template_name)
        ctx = RequestContext({}, self.params)
        return tmpl.render(ctx)

    def rendered_child(self):
        return self.rendered_template("child.html")

    def rendered_child_no_extends(self):
        return self.rendered_template("child_no_extends.html")

    def rendered_base(self):
        return self.rendered_template("base.html")

    def rendered_base_no_extends(self):
        return self.rendered_template("base_no_extends.html")

    def test_template_performance_no_extends(self):
        timer = timeit.Timer(self.rendered_child_no_extends)
        print u"This test standalone rendering {0}".format(timer.timeit(5000))

    def test_template_performance_extends(self):
        timer = timeit.Timer(self.rendered_child)
        print u"This test extends {0}".format(timer.timeit(5000))

    def test_template_performance_include_extends(self):
        timer = timeit.Timer(self.rendered_base)
        print u"This test include and extends {0}".format(timer.timeit(5000))

    def test_template_performance_include_no_extends(self):
        timer = timeit.Timer(self.rendered_base_no_extends)
        print u"This test include {0}".format(timer.timeit(5000))


