from setuptools import setup, find_packages

VERSION = '1.0.1'
setup(name='coco-caption',
      version=VERSION,
      url="https://github.com/tylin/coco-caption",
      description="Microsoft COCO Caption Evaluation",
      entry_points={
          'console_scripts': ['evaluate-coco-captions=pycocoevalcap.__main__:main']
      },
      requires=['numpy', 'matplotlib'],
      packages=find_packages())
