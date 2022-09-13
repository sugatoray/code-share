# cspell: disable

"""
User Defined Functions (udfs).

.. warning:: Using Math Symbols and Equations 💟

    <details>
    <summary>Click to expand</summary>
    <p markdown="1">

    The documentation also supports math symbols.

    $$ \Gamma(x) = \int_{0}^{n} \psi(x) f(n - x)\,dx $$

    </p>
    </details>

.. note:: How to Generate Documentation 📚

    <details>
    <summary>Click to expand</summary>
    <p markdown="1">

    The documentation is generated with 🔗 [`pdoc`](https://pdoc.dev/).

    🔥 Install `pdoc` first.

    ```sh
    pip install pdoc
    ```

    #### 📚 A. Generate Docs and View

    Use the following command to generate it for this file.

    **Note:** *Run the command from the same directory as
     this file. This will not create any files for the
     documentation; it will only render the docs on a local
     server and make it available for viewing.*

    ```sh
    pdoc -d google -h localhost -n -p 5555 --math --show-source udfs.py
    ```

    Running this will show something like this and start hosting the generated docs on a local server.

    - `pdoc server ready at http://localhost:5555`

    #### 💡 B. Saving Generated Docs

    Alternatively, if you want to generate the documentation and open the html file(s) later as well, use the following command.

    👉 This will not open any browser or start any server.

    ```sh
    mkdir -p docs && pdoc -o ./docs -d google --math --show-source udfs.py
    ```

    </p>
    </details>
"""

# %%
# list of imports
import os
import sys
import pdoc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# extract absolute path of the directory where this file lives.
HERE = os.path.dirname(os.path.abspath(__file__))

# define pdoc docformat
__docformat__ = "google"

# %%

def converter(val: str, method: str = "bin") -> int:
    """Number converter (to bin and hex).

    Converts a string of base 10 number into binary or haxadecimal output of its nth byte (n = 4).


    TODO: add more meaningful one-liner description later

    Args:
        val (str): A base 10 number as a string.
        method (str, optional): Method of intermediate conversion.
                                Choose from {``"bin"``, ``"hex"``}.
                                Defaults to ``"bin"``.

    Returns:
        int: A base 10 integer.

    Usage:

        ```python
        val = "96233165882300781066336604175414015767"
        converter(val, method="bin")
        ```

    .. danger:: Note

        This is equivalent to:

        For ``Binary``:

        ```python
        val = "96233165882300781066336604175414015767"
        bval = bin(int(val, 10))
        target = bval[2:].zfill(128)[24:32]
        int(target, 2)
        ```

        For ``Hexadecimal``:

        ```python
        val = "96233165882300781066336604175414015767"
        hval = hex(int(val, 10))
        target = hval[2:].zfill(32)[6:8]
        int(target, 16)
        ```
    """

    if method == "bin":
        # binary number
        base = 2
        val_length = 128
        func = bin  # type: ignore
        # target_range: [24:32]; 24 to 31 (excludes 32)
        target_range = (24, 32)
    elif method == "hex":
        # hexadecimal number
        base = 16
        val_length = 32  # 4 binary bits == 1 hex bit
        func = hex  # type: ignore
        # target_range: [6:8]; 6 to 7 (excludes 8)
        target_range = (6, 8)
    elif method == "dec":
        # decimal number
        base = 10
        val_length = len(val)
        def func(x): return x
        target_range = (0, val_length)

    val = func(int(val, 10))  # type: ignore
    target = val[2:].zfill(val_length)[slice(*target_range)]
    result = int(target, base)

    return result


# %%
if __name__ == "__main__":

    # %%
    # 💡 When running as a standalone module,
    #    append to Python Path.
    # 👉 This helps is using relative paths of other files and
    #    data-files with no room for error. You will not need
    #    to navigate to the folder where this file lives.
    # 👉 Running it from anywhere will have the same effect.
    sys.path.append(HERE)

    # %%
    val = "96233165882300781066336604175414015767"
    result = converter(val, method="bin")
    # Define an on-the-fly lambda function (anonymous function)
    # to reuse as many times as probing is necessary
    probe = lambda x, label, prefix="\t👉 ": print(
        f"{prefix}{label}: {x} | type: {type(x)}")
    print("\n🔥 Inspect input and result:\n\n")
    probe(val, "val")
    probe(result, "result")
