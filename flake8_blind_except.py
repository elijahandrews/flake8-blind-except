try:
    import pycodestyle
except ImportError:
    import pep8 as pycodestyle
import re

__version__ = '0.2.1'

BLIND_EXCEPT_REGEX = re.compile(r'(^[ \t]*except(.*\b(Base)?Exception\b.*)?:)')  # noqa

def check_blind_except(physical_line):
    """Check for blind except statements.

    >>> check_blind_except('except:')
    (0, 'B901 blind except: statement')
    >>> check_blind_except('except Exception:')
    (0, 'B902 blind except Exception: statement')
    >>> check_blind_except('except  Exception as exc:')
    (0, 'B902 blind except Exception: statement')
    >>> check_blind_except('except ValueError, Exception as exc:')
    (0, 'B902 blind except Exception: statement')
    >>> check_blind_except('except Exception, ValueError as exc:')
    (0, 'B902 blind except Exception: statement')
    >>> check_blind_except('except BaseException as exc:')
    (0, 'B902 blind except Exception: statement')
    >>> check_blind_except('except GoodException as exc:  # except:')
    >>> check_blind_except('except ExceptionGood as exc:')
    >>> check_blind_except('except Exception')  # only trigger with trailing colon
    >>> check_blind_except('some code containing except: in string')
    """
    if pycodestyle.noqa(physical_line):
        return
    match = BLIND_EXCEPT_REGEX.search(physical_line)
    if match:
        if match.group(2) is None:
            return match.start(), 'B901 blind except: statement'
        else:
            return match.start(), 'B902 blind except Exception: statement'

check_blind_except.name = 'flake8-blind-except'
check_blind_except.version = __version__
