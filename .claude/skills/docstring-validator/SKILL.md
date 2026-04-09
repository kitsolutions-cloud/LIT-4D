---
name: docstring-validator
description: >
  Validate and improve Python docstrings using Google style. Use this skill whenever the user
  shares Python code (pasted or as a .py file) and asks to check, validate, review, audit,
  fix, improve, or generate docstrings. Also trigger when the user says things like "are my
  docstrings good?", "check my docs", "document this function", or "does this docstring make
  sense?". Do not wait for explicit keywords — if Python code is present and docstring quality
  is relevant, use this skill.
---

# Python Docstring Validator (Google Style)

Validate and improve Python docstrings by analyzing what each class/function actually does,
then comparing that understanding against the existing docstring and suggesting improvements.

---

## Input

Accept code in two ways:

- **Pasted inline**: Extract all Python classes and functions directly from the message.
- **Uploaded `.py` file**: Read from `/mnt/user-data/uploads/<filename>`. Use the
  `file-reading` skill if needed to load the file content first.

---

## Step-by-step workflow

### 1. Parse the code

Identify every **class** and **function/method** in the provided code. Build a list of targets:

- Class name + its body (including `__init__`)
- Each method/function: name, signature (parameters + type hints if present), body

### 2. Understand what each target does

For each class/function, read its **implementation** carefully:

- What is its responsibility / purpose?
- What do the parameters represent and what types are expected?
- What does it return, and under what conditions?
- What exceptions can it raise, and when?
- Are there any non-obvious behaviors, side effects, or important edge cases?

This understanding is the **ground truth** you will use to evaluate the docstring.

### 3. Evaluate the existing docstring

For each target check the following. Note any issues found.

| Section          | What to check                                                                     |
|------------------|-----------------------------------------------------------------------------------|
| **Summary line** | One line, imperative mood, accurate, not vague. Does it match what the code does? |
| **Description**  | Present only if needed. Accurate, adds context not obvious from the signature.    |
| **Args**         | Every parameter documented. Types match hints/usage. Descriptions are meaningful. |
| **Returns**      | Present if the function returns a value. Type and description are accurate.       |
| **Raises**       | Every raised exception documented with the condition that triggers it.            |
| **Examples**     | Present for public APIs / non-trivial functions. Valid, runnable, illustrative.   |

**Accuracy issues** (docstring says something wrong or misleading) are higher priority than
**completeness issues** (a section is missing or thin).

### 4. Handle missing docstrings

If a function/class has **no docstring at all**, do **not** silently generate one.
Instead, tell the user:

> `<FunctionName>` has no docstring. Would you like me to generate one from scratch,
> or skip it?

Wait for their response before proceeding for that target. You can batch this question
for all missing-docstring targets in one message if there are several.

### 5. Produce a diff for each target

For every target that needs changes (or is being generated from scratch), present a
**before / after diff** using this format:

````
### `ClassName.method_name`

**Issues found:**
- <brief bullet list of problems>

**Suggested docstring:**

```diff
- """Old summary line here.
-
- Args:
-     x: something vague
- """
+ """Imperative-mood accurate summary here.
+
+ Longer description if needed.
+
+ Args:
+     x (int): Clear description of what x represents.
+
+ Returns:
+     bool: Description of what is returned and when.
+
+ Raises:
+     ValueError: When x is negative.
+
+ Example:
+     >>> result = method_name(5)
+     >>> print(result)
+     True
+ """
```
````

Lines prefixed with `-` are removed; lines prefixed with `+` are added.
If there is no existing docstring, show only `+` lines.

### 6. Summary report

After all diffs, output a brief summary table:

| Target            | Status         | Issues                      |
|-------------------|----------------|-----------------------------|
| `MyClass`         | ✅ OK           | —                           |
| `MyClass.process` | ⚠️ Improved    | Missing Returns, vague Args |
| `helper_func`     | ❌ No docstring | Generated from scratch      |

---

## Official Google Style Guide Rules (§3.8)

These rules are sourced directly from https://google.github.io/styleguide/pyguide.html.
Apply them all during validation.

---

### §3.8.1 — Docstring basics

- Always use `"""triple double quotes"""`.
- One-line docstrings: opening and closing `"""` on the same line as the content.
- Multi-line docstrings: summary on the first line (same line as opening `"""`), blank line, then body, closing `"""` on
  its own line.

```python
# One-liner (only for truly simple/obvious functions)
def add(a, b):
    """Return the sum of a and b."""


# Multi-line
def complex_func(a, b):
    """Compute something non-trivial.

    Extended explanation here.

    Args:
        ...
    """
```

---

### §3.8.2 — Module docstrings

Every module should begin with a docstring:

```python
"""One-line summary of the module, terminated by a period.

Leave one blank line. The rest describes the module's overall purpose,
exported classes, functions, and/or a usage example.

Typical usage example:
    foo = ClassFoo()
    bar = foo.function_bar()
"""
```

Flag module-level docstrings as missing if the file has none.

---

### §3.8.3 — Functions and Methods

**A docstring is MANDATORY when a function has ANY of these properties:**

- Part of the public API (no leading `_`)
- Non-trivial size (more than a few lines)
- Non-obvious logic

The docstring should give enough information to write a call to the function
**without reading its code**. Describe calling syntax and semantics; generally
avoid describing implementation details unless they affect usage.

**Args section rules (§3.8.3):**

- Document every parameter **except** `self` and `cls`.
- Format: `name (type): Description.` — but **omit the type** if the function
  already has type annotations in the signature (no duplication).
- For optional params: `name (type, optional): Description. Defaults to X.`
- For `*args` / `**kwargs`: document them too.

**Returns section rules:**

- Omit if the function returns `None` or is a constructor.
- Format: `type: Description of what is returned.`
- For complex return types (dicts, tuples), describe the structure and keys.

**Yields (generators — §2.9):**

- Use `Yields:` instead of `Returns:` for generator functions.

**Raises section rules (§2.4 + §3.8.3):**

- Document only exceptions the function **explicitly raises** or **intentionally
  lets propagate** as part of its contract.
- Do NOT document exceptions raised to signal API misuse (e.g., a `ValueError`
  raised as an internal precondition guard — that's an implementation detail,
  not a contract guarantee).
- Format: `ExceptionType: Condition that triggers it.`

**Example section:**

- Use `>>>` doctest style.
- Required for public APIs and non-trivial functions.
- Must be correct and runnable.

---

### §3.8.3.1 — Overridden Methods

A method decorated with `@override` (from `typing` or `typing_extensions`)
does **not** need a docstring **unless**:

- Its behavior materially refines the base method's contract, OR
- There are additional side effects or details to document.

If a docstring is present on an override, it only needs to describe the
differences from the parent.

---

### §3.8.4 — Classes

- The class docstring goes on the class, not on `__init__`.
- It should describe the class and its public interface.
- List public **instance attributes** in an `Attributes:` section (same format as Args).
- `__init__` should have its own docstring only if its logic is non-obvious;
  constructor arguments go in the class docstring or `__init__` docstring, not both.

```python
class SampleClass:
    """Summary of class purpose.

    Longer description of the class if needed.

    Attributes:
        likes_spam (bool): Whether the instance likes spam.
        eggs (int): Number of eggs the instance has.
    """

    def __init__(self, likes_spam: bool = False):
        self.likes_spam = likes_spam
        self.eggs = 0
```

---

### §3.8.6 — Punctuation, Spelling, and Grammar

These are **style violations** to flag during validation:

- Every sentence in a docstring must **end with a period** (including the summary line).
- The summary line must use **imperative mood**: "Return", "Calculate", "Validate"
  — NOT "Returns", "Calculates", or "This function returns...".
- Correct capitalization: first word of each sentence capitalized.
- No placeholder or stub text: "TODO", "...", "Description here", "TBD".
- Proper spelling (flag obvious typos).
- No truncated or unfinished sentences.

---

## Canonical format template

```python
def fetch_rows(
    table: str,
    keys: Sequence[str],
    require_all_keys: bool = False,
) -> Mapping[str, Any]:
    """Fetch rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table. Silly things may happen if other_silly_variable
    is not None.

    Args:
        table: The table from which to fetch rows.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        require_all_keys: If True, only rows with values set for all keys
            will be returned.

    Returns:
        A dict mapping keys to the corresponding table row data fetched.
        Each row is represented as a tuple of strings. For example:
        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader')}

    Raises:
        IOError: An error occurred accessing the table.
    """
```

> Note: types are omitted from Args because the signature already has type annotations.

---

## Quality bar for "OK"

Mark a docstring as ✅ OK only if ALL of the following pass:

| Check                                                  | Rule source |
|--------------------------------------------------------|-------------|
| Summary is imperative mood and ends with a period      | §3.8.6      |
| Summary fits on one line                               | §3.8.1      |
| All public params documented (not `self`/`cls`)        | §3.8.3      |
| No type duplication when type annotations exist        | §3.8.3      |
| `Returns:` present for non-None returns                | §3.8.3      |
| Generators use `Yields:` not `Returns:`                | §2.9        |
| Only contract-level exceptions in `Raises:`            | §2.4        |
| Public class has `Attributes:` if it has public attrs  | §3.8.4      |
| `@override` methods don't needlessly repeat parent doc | §3.8.3.1    |
| No placeholder text, typos, or unfinished sentences    | §3.8.6      |

If any check fails, suggest an improvement.

---

## Tone

Be constructive, not pedantic. When something is mostly fine, say so. Focus feedback on
accuracy and clarity, not stylistic nitpicks. If the existing docstring is good, say it's ok.