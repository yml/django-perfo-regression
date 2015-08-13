# Template rendering time

I have recently notice a very significant slow down on a web site doing extensive usage of `include` & `extends` during a migration from 1.6.11 to 1.8.3.

This lead me to create this very simple django project containing tests exercising these features. I am using the python `timeit` module to clock the time to perform each tasks.

I have created 2 branches with 2 different settings set:

* `master` DEBUG=True that mimics a development environment
* `production_settings` DEBUG=False and with `cached.Loader` mimics a simplified production setup


## master

![DEBUG=True](https://docs.google.com/spreadsheets/d/1v-cXcx8lLOF7sphtvdofU-30GmpPCyvgn1TjIRJk4OM/pubchart?oid=142700709&format=image)

Since **Django 1.7** the time required to render templates with `include` and `extends` almost doubled.

## production_settings

![cached.Loader & DEBUG=False](https://docs.google.com/spreadsheets/d/1v-cXcx8lLOF7sphtvdofU-30GmpPCyvgn1TjIRJk4OM/pubchart?oid=1717835180&format=image)

**Django 1.8.3** introduced a significant slow down in the **1.8** family that was other wise faster than the previous releases.

## Additional information

* [django ticket](https://code.djangoproject.com/ticket/25228#ticket)
* [spreadsheet with my results](https://docs.google.com/spreadsheets/d/1v-cXcx8lLOF7sphtvdofU-30GmpPCyvgn1TjIRJk4OM/edit#gid=0)

## Update August 13th 2015

`git bisect` between 1.8.2 and 1.8.3 point its finger on the following commit:

```
b16f84f15b1344d2a3df8149565cfc8de803eb77 is the first bad commit
commit b16f84f15b1344d2a3df8149565cfc8de803eb77
Author: Tim Graham <timograham@gmail.com>
Date:   Wed May 27 09:19:19 2015 -0400

    [1.8.x] Refs #24836 -- Reverted "Simplified the lazy CSRF token implementation in csrf context processor."
    
    This reverts commit 8099d33b6553c9ee7de779ae9d191a1bf22adbda as it caused
    a regression that cannot be solved without changing force_text() which has
    a small risk of introducing regressions. This change will remain in master
    along with an update to force_text().

:040000 040000 79f27245b250a4ac0c65a4ccef0b8db107432312 6c6a96934b66615d663375cc13199cf50c6fd1ec M      django
:040000 040000 c977299c605629e42fd2ec7bb53264d5ac25db78 9eef450849404da0e8f20c292b8aa8b544176681 M      docs
:040000 040000 96fa0ceb7be7bd9ca14eded3ca98478a22ce8f39 e3c95cc6052e620319c7ef2d64a1716825839414 M      tests
````

Here it is a link to the [https://github.com/django/django/commit/b16f84f15b1344d2a3df8149565cfc8de803eb77 diff on github]
