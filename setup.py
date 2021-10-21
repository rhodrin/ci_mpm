try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='simple_functions',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description="Environment for playing with CI.",
      long_descritpion="""Playing with CI.""",
      url='https://github.com/acse-2020',
      author="Imperial College London",
      author_email='rhodri.nelson@imperial.ac.uk',
      packages=['simple_functions'])
