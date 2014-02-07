from setuptools import setup

def get_version(fname='flake8_blind_except.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])

def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-blind-except',
    description='A flake8 extension that checks for blind except: statements',
    long_description=get_long_description(),
    keywords='flake8 except exception',
    version=get_version(),
    author='Elijah Andrews',
    author_email='elijahcandrews@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'B90 = flake8_blind_except:check_blind_except'
        ],
    },
    url='https://github.com/elijahandrews/flake8-blind-except',
    license='MIT',
    py_modules=['flake8_blind_except'],
    zip_safe=False,
)
