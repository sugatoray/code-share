### An example of creating a python module in Google Colab

You can also find the same in a jupyter notebook :fire: [here](https://github.com/sugatoray/code-share/blob/master/notebooks/demo_making_python_modules.ipynb).

<details>
<summary>Click to expand and see the example</summary>
<p>

Install `tree` in colab so you could see the package directory tree conveniently.

```sh
%%capture
! sudo apt install tree
```

Create the package root directory (this will be the name of the repository, if you were to sync with GitHub).

```python
import os

os.chdir("/content")

PACKAGE_ROOT = "humpty_dumpty"
PACKAGE_NAME = "humpty"
COLAB_HOME = os.path.abspath(os.curdir)
PACKAGE_ROOT_PATH = os.path.join(COLAB_HOME, PACKAGE_ROOT)
print(f"""\n
PACKAGE_ROOT: {PACKAGE_ROOT}
PACKAGE_NAME: {PACKAGE_NAME}
COLAB_HOME: {COLAB_HOME}
\n""")

# Create directory
# ! mkdir -p {PACKAGE_ROOT}
os.makedirs(PACKAGE_ROOT_PATH, exist_ok=True)
# Visualize directory structure
! tree
```

Change directory: `cd` into `PACKAGE_ROOT` and create package directory with `PACKAGE_NAME` variable.

```python
# Change directory and create package dir
os.chdir(PACKAGE_ROOT_PATH)
os.makedirs(PACKAGE_NAME, exist_ok=True)
! tree .
```

Create a `__init__.py` file inside `PACKAGE_NAME` folder. This makes the folder act like a python module.

```python
! touch {PACKAGE_NAME}/__init__.py
! tree .
```

Now let's add a python file `humpty.py` with a few functions in it.

```python
%%writefile {PACKAGE_NAME}/dumpty.py

POOR_GUY: str = "Humpty Dumpty"

def whoisthis() -> str:
    return POOR_GUY

def hasfallen(name: str) -> bool:
    return name.strip() == POOR_GUY

if __name__ == "__main__":
    # test-1
    print(f"This is: {whoisthis()}")
    # test-2
    name = "Humpty"
    print(f"Has {name} fallen? {hasfallen(name)}") # false
    # test-3
    name = "Humpty Dumpty"
    print(f"Has {name} fallen? {hasfallen(name)}") # true
```

Check the project structure with `tree` command.

```python
! tree .
```

Test driven development helps in identifying and correcting errors early on. So, let's run `dumpty.py` and see if it runs without errors.

```python
! python {PACKAGE_NAME}/dumpty.py
```

Now let's create another folder `dinner` under the `PACKAGE_NAME` folder and make that also a python module.

```python
# Create a folder: dinner
! mkdir -p {PACKAGE_NAME}/dinner

# Convert the created folder into a python 
# module by adding __init__.py file.
! touch {PACKAGE_NAME}/dinner/__init__.py
! tree .
```

Now let's add another python file `invitation.py` inside `dinner` folder.

```python
%%writefile {PACKAGE_NAME}/dinner/invitation.py

def invite(name: str, date: str="2022-02-02") -> str:
    body = f"""
    Dear {name},

    You and your family are invited to the dinner at our mansion on next Saturday! 
    Dinner starts at 7 pm.

    Regards
    --
    Sir Augustine Medvedev
    Dated: {date}
    """
    return body
```

Let's check the directory structure once again.

```python
! tree .
```

## Moment of Truth: Import and Test the Python Module

Let's import and try out the module and it's functions we just created.

```python
from humpty.dinner.invitation import invite
from humpty import hasfallen

name = "Humpty"
if not hasfallen(name):
    print(invite(name=name, date="2022-06-11"))
```

</p>
</details>
