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

[django ticket](https://code.djangoproject.com/ticket/25228#ticket)
[spreadsheet with my results](https://docs.google.com/spreadsheets/d/1v-cXcx8lLOF7sphtvdofU-30GmpPCyvgn1TjIRJk4OM/edit#gid=0)
