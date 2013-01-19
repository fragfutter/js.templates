from setuptools import setup, find_packages

version = '2013.01.19'

setup(name='js.templates',
      version=version,
      description="lightweight, fast & powerful JavaScript templating engine with zero dependencies",
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Christoph Handel',
      author_email='',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      setup_requires=['setuptools-git'],
      install_requires=[
          'fanstatic',
      ],
      entry_points={
          'fanstatic.libraries': ['js_templates = js.templates:library', ],
      }
      )
