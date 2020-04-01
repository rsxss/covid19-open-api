from setuptools import setup, find_packages


with open('README.md', 'r') as readme, open('requirements.txt', 'r') as requirements:
    long_description = readme.read()
    dependencies = requirements.read()

    kwargs = {
        'name': 'covid19-open-api',
        'version': '0.0.3',
        'author': 'Natworpong Loyswai',
        'author_email': 'Natworpong.Loyswai@mail.kmutt.ac.th',
        'description': 'Thai Covid-19 status',
        'long_description': long_description,
        'long_description_content_type': 'text/markdown',
        'url': 'https://github.com/rsxss/covid19-open-api',
        'packages': find_packages(),
        'classifiers': [
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        'keywords': ['covid19'],
        'install_requires': dependencies
    }

    setup(**kwargs)
