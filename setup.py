from setuptools import setup

setup(name='turtle-kernel',
      version='0.1.0',
      description='A simple echo turtle kernel for Jupyter/IPython',
      long_description='A simple echo turle kernel for Jupyter/IPython, based on MetaKernel Echo',
      url='https://github.com/calysto/metakernel/tree/master/metakernel_echo',
      author='Douglas Blank',
      author_email='doug.blank@gmail.com',
      py_modules=['turtle_kernel'],
      install_requires=['metakernel'],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
          'Topic :: System :: Shells',
      ]
)