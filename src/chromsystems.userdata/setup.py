from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='chromsystems.userdata',
      version=version,
      description="Chromsystems Userdata and member management.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Vorwaerts Werbung GbR',
      author_email='hallo@vorwaerts-werbung.de',
      url='http://dist.vorwaerts-werbung.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['chromsystems'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'plone.app.users',
          'plone.directives.form',
          'plone.app.z3cform',
          'plone.namedfile [blobs]',
          'plone.formwidget.namedfile',
          'five.grok',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
