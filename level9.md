

## Level 9

so now we want to create a gcp bucket with ock data

they recommended to use Lorem
simple example fro the pypi page

```python
import lorem

s = lorem.sentence()  # 'Eius dolorem dolorem labore neque.'
p = lorem.paragraph()
t = lorem.text()
```

more complex example

```python
from lorem.text import TextLorem

# separate words by '-'
# sentence length should be between 2 and 3
# choose words from A, B, C and D
lorem = TextLorem(wsep='-', srange=(2,3), words="A B C D".split())

s1 = lorem.sentence()  # 'C-B.'
s2 = lorem.sentence()  # 'C-A-C.'
```

## steps

as usual, we will first create a virtual env
than install the necc dependencies

after that we will create a new bucket with our python code
and write some mock data to it
we want to hide a flag inside the mock data
