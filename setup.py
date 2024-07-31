from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='nepalikit',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'torch>=2.3.1',
        'sentencepiece==0.2.0',
        'regex'
    ],
    include_package_data=True,
    package_data={
        'nepalikit': ['tokenization/sentencepiece/model/NepaliKit_sentencepiece.model'],
    },
    entry_points={
        'console_scripts': [
            'nepalikit-cli = nepalikit.__main__:main',
        ],
    },
    author='Prabhash Kumar Jha',
    author_email='prabhashj07@gmail.com',
    description='A Nepali language processing library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/prabhashj07/nepalikit.git',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Nepali',
        'Topic :: Text Processing :: Linguistic',
    ],
    python_requires='>=3.7',
    project_urls={
        'Bug Reports': 'https://github.com/prabhashj07/nepalikit/issues',
        'Source': 'https://github.com/prabhashj07/nepalikit/',
},
)

