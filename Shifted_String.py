import re
def is_shifted(a, b):
    a_shifted=a+a
    regex=re.compile(pattern=b)
    return bool(re.findall(pattern=regex,string=a_shifted))
  
print(is_shifted('abcde', 'cdeab'))
# True