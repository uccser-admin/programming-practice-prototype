"""Data for Python 3 style errors.

The following fields are rendered as HTML.
  - solution
  - explanation
"""

DATA = {
    "E101": {
        "original_message": "indentation contains mixed spaces and tabs",
        "title_templated": False,
        "title": "Line is indented using a mixture of spaces and tabs.",
        "solution": "You should indent your code using only spaces.",
        "explanation": "Python expects the indentation method to be consistent line to line. Spaces are the preferred indentation method."
    },
    "E111": {
        "original_message": "indentation is not a multiple of four",
        "title_templated": False,
        "title": "Line has an indentation level that is not a multiple of four.",
        "solution": "Ensure that the first indentation level is 4 spaces, the second indentation level is 8 spaces and so on.",
        "explanation": ""
    },
    "E112": {
        "original_message": "expected an indented block",
        "title_templated": False,
        "title": "Line is not indented at the correct level.",
        "solution": "Add indentation to this line until it is indented at the correct level.",
        "explanation": ""
    },
    "E113": {
        "original_message": "unexpected indentation",
        "title_templated": False,
        "title": "Line is indented when it shouldn't be.",
        "solution": "Remove indentation from this line until it is indented at the correct level.",
        "explanation": ""
    },
    "E114": {
        "original_message": "indentation is not a multiple of four (comment)",
        "title_templated": False,
        "title": "Line has an indentation level that is not a multiple of four.",
        "solution": "Ensure that the first indentation level is 4 spaces, the second indentation level is 8 spaces and so on.",
        "explanation": ""
    },
    "E115": {
        "original_message": "expected an indented block (comment)",
        "title_templated": False,
        "title": "Line is not indented at the correct level.",
        "solution": "Add indentation to this line until it is indented at the correct level.",
        "explanation": "Comments should be indented relative to the code block they are in."
    },
    "E116": {
        "original_message": "unexpected indentation (comment)",
        "title_templated": False,
        "title": "Line is indented when it shouldn't be.",
        "solution": "Remove indentation from this line until it is indented at the correct level.",
        "explanation": ""
    },
    "E117": {
        "original_message": "over-indented",
        "title_templated": False,
        "title": "Line has too many indentation levels.",
        "solution": "Remove indentation from this line until it is indented at the correct level.",
        "explanation": ""
    },
    # E121 ignored by default
    "E121": {
        "original_message": "continuation line under-indented for hanging indent",
        "title_templated": False,
        "title": "Line is less indented than it should be.",
        "solution": "Add indentation to this line until it is indented at the correct level.",
        "explanation": ""
    },
    "E122": {
        "original_message": "continuation line missing indentation or outdented",
        "title_templated": False,
        "title": "Line is not indented as far as it should be or is indented too far.",
        "solution": "Add or remove indentation levels until it is indented at the correct level.",
        "explanation": ""
    },
    # E123 ignored by default
    "E123": {
        "original_message": "closing bracket does not match indentation of opening bracket’s line",
        "title_templated": False,
        "title": "Line has a closing bracket that does not match the indentation level of the line that the opening bracket started on.",
        "solution": "Add or remove indentation of the closing bracket so it matches the indentation of the line that the opening bracket is on.",
        "explanation": ""
    },
    "E124": {
        "original_message": "closing bracket does not match visual indentation",
        "title_templated": False,
        "title": "Line has a closing bracket that does not match the indentation of the opening bracket.",
        "solution": "Add or remove indentation of the closing bracket so it matches the indentation of the opening bracket.",
        "explanation": ""
    },
    "E125": {
        "original_message": "continuation line with same indent as next logical line",
        "title_templated": False,
        "title": "Line has a continuation that should be indented one extra level so that it can be distinguished from the next logical line.",
        "solution": "Add an indentation level to the line continuation so that it is indented one more level than the next logical line.",
        "explanation": "Continuation lines should not be indented at the same level as the next logical line. Instead, they should be indented to one more level so as to distinguish them from the next line."
    },
    # E126 ignored by default
    "E126": {
        "original_message": "continuation line over-indented for hanging indent",
        "title_templated": False,
        "title": "Line is indented more than it should be.",
        "solution": "Remove indentation from this line until it is indented at the correct level.",
        "explanation": ""
    },
    "E127": {
        "original_message": "continuation line over-indented for visual indent",
        "title_templated": False,
        "title": "Line is indented more than it should be.",
        "solution": "Remove indentation from this line until it is indented at the correct level.",
        "explanation": ""
    },
    "E128": {
        "original_message": "continuation line under-indented for visual indent",
        "title_templated": False,
        "title": "Line is indented less than it should be.",
        "solution": "Add indentation to this line until it is indented at the correct level.",
        "explanation": ""
    },
    "E129": {
        "original_message": "visually indented line with same indent as next logical line",
        "title_templated": False,
        "title": "Line has the same indentation as the next logical line.",
        "solution": "Add an indentation level to the visually indented line so that it is indented one more level than the next logical line.",
        "explanation": "A visually indented line that has the same indentation as the next logical line is hard to read."
    },
    "E131": {
        "original_message": "continuation line unaligned for hanging indent",
        "title_templated": False,
        "title": "Line is not aligned correctly for a hanging indent.",
        "solution": "Add or remove indentation so that the lines are aligned with each other.",
        "explanation": ""
    },
    # E133 ignored by default
    # "E133": {
    #     "original_message": "closing bracket is missing indentation",
    #     "title_templated": False,
    #     "title": "",
    #     "solution": "",
    #     "explanation": "",
    # },
    "E201": {
        "original_message": "whitespace after '{character}'",
        "title_templated": True,
        "title": "Line contains {article} {character_description} that has a space after it.",
        "solution": "Remove any spaces that appear after the `{character}` character.",
        "explanation": ""
    },
    "E202": {
        "original_message": "whitespace before '{character}'",
        "title_templated": True,
        "title": "Line contains {article} {character_description} that has a space before it.",
        "solution": "Remove any spaces that appear before the `{character}` character.",
        "explanation": ""
    },
    "E203": {
        "original_message": "whitespace before '{character}'",
        "title_templated": True,
        "title": "Line contains {article} {character_description} that has a space before it.",
        "solution": "Remove any spaces that appear before the `{character}` character.",
        "explanation": ""
    },
    "E211": {
        "original_message": "whitespace before '{character}'",
        "title_templated": True,
        "title": "Line contains {article} {character_description} that has a space before it.",
        "solution": "Remove any spaces that appear before the `{character}` character.",
        "explanation": ""
    },
    "E221": {
        "original_message": "multiple spaces before operator",
        "title_templated": False,
        "title": "Line has multiple spaces before an operator.",
        "solution": "Remove any extra spaces that appear before the operator on this line.",
        "explanation": ""
    },
    "E222": {
        "original_message": "multiple spaces after operator",
        "title_templated": False,
        "title": "Line has multiple spaces after an operator.",
        "solution": "Remove any extra spaces that appear after the operator on this line.",
        "explanation": ""
    },
    "E223": {
        "original_message": "tab before operator",
        "title_templated": False,
        "title": "Line contains a tab character before an operator.",
        "solution": "Remove any tab characters that appear before the operator on this line. Operators should only have one space before them.",
        "explanation": ""
    },
    "E224": {
        "original_message": "tab after operator",
        "title_templated": False,
        "title": "Line contains a tab character after an operator.",
        "solution": "Remove any tab characters that appear after the operator on this line. Operators should only have one space after them.",
        "explanation": ""
    },
    "E225": {
        "original_message": "missing whitespace around operator",
        "title_templated": False,
        "title": "Line is missing whitespace around an operator.",
        "solution": "Ensure there is one space before and after all operators.",
        "explanation": ""
    },
    # E226 ignored by default
    "E226": {
        "original_message": "missing whitespace around arithmetic operator",
        "title_templated": False,
        "title": "Line is missing whitespace around an arithmetic operator (`+`, `-`, `/` and `*`).",
        "solution": "Ensure there is one space before and after all arithmetic operators (`+`, `-`, `/` and `*`).",
        "explanation": ""
    },
    "E227": {
        "original_message": "missing whitespace around bitwise or shift operator",
        "title_templated": False,
        "title": "Line is missing whitespace around a bitwise or shift operator (`<<`, `>>`, `&`, `|`, `^`).",
        "solution": "Ensure there is one space before and after all bitwise and shift operators (`<<`, `>>`, `&`, `|`, `^`).",
        "explanation": ""
    },
    "E228": {
        "original_message": "missing whitespace around modulo operator",
        "title_templated": False,
        "title": "Line is missing whitespace around a modulo operator (`%`).",
        "solution": "Ensure there is one space before and after the modulo operator (`%`).",
        "explanation": ""
    },
    "E231": {
        "original_message": "missing whitespace after ‘,’, ‘;’, or ‘:’",
        "title_templated": False,
        "title": "Line is missing whitespace around one of the following characters: `,` `;` and `:`.",
        "solution": "Ensure there is one space before and after any of the following characters: `,` `;` and `:`.",
        "explanation": ""
    },
    # E241 ignored by default
    "E241": {
        "original_message": "multiple spaces after ‘,’",
        "title_templated": False,
        "title": "Line has multiple spaces after the `,` character.",
        "solution": "Ensure there is one space before and after any `,` characters.",
        "explanation": ""
    },
    # E242 ignored by default
    "E242": {
        "original_message": "tab after ‘,’",
        "title_templated": False,
        "title": "Line contains a tab character after the `,` character.",
        "solution": "Remove any tab characters and ensure there is one space before and after any `,` characters.",
        "explanation": ""
    },
    "E251": {
        "original_message": "unexpected spaces around keyword / parameter equals",
        "title_templated": False,
        "title": "Line contains spaces before or after the `=` in a function definition.",
        "solution": "Remove any spaces that appear either before or after the `=` character in your function definition.",
        "explanation": ""
    },
    "E261": {
        "original_message": "at least two spaces before inline comment",
        "title_templated": False,
        "title": "Line contains an inline comment that does not have 2 spaces before it.",
        "solution": "Ensure that your inline comment has 2 spaces before the `#` character.",
        "explanation": ""
    },
    "E262": {
        "original_message": "inline comment should start with ‘# ‘",
        "title_templated": False,
        "title": "Comments have a space between the `#` character and the comment message.",
        "solution": "Ensure that your inline comment has a space between the `#` character and the comment message.",
        "explanation": ""
    },
    "E265": {
        "original_message": "block comment should start with ‘# ‘",
        "title_templated": False,
        "title": "Comments should start with a `#` character and have one space between the `#` character and the comment itself.",
        "solution": "Ensure that your block comment has a space between the `#` character and the comment message.",
        "explanation": ""
    },
    "E266": {
        "original_message": "too many leading ‘#’ for block comment",
        "title_templated": False,
        "title": "Comments should only start with a single `#` character.",
        "solution": "Ensure your comment only starts with one `#` character.",
        "explanation": ""
    },
    "E271": {
        "original_message": "multiple spaces after keyword",
        "title_templated": False,
        "title": "Line contains more than one space after a keyword.",
        "solution": "Ensure there is only one space after any keywords.",
        "explanation": ""
    },
    "E272": {
        "original_message": "multiple spaces before keyword",
        "title_templated": False,
        "title": "Line contains more than one space before a keyword.",
        "solution": "Ensure there is only one space before any keywords.",
        "explanation": ""
    },
    "E273": {
        "original_message": "tab after keyword",
        "title_templated": False,
        "title": "Line contains a tab character after a keyword.",
        "solution": "Ensure there is only one space after any keywords.",
        "explanation": ""
    },
    "E274": {
        "original_message": "tab before keyword",
        "title_templated": False,
        "title": "Line contains a tab character before a keyword.",
        "solution": "Ensure there is only one space before any keywords.",
        "explanation": ""
    },
    "E275": {
        "original_message": "missing whitespace after keyword",
        "title_templated": False,
        "title": "Line is missing a space after a keyword.",
        "solution": "Ensure there is one space after any keywords.",
        "explanation": ""
    },
    "E301": {
        "original_message": "expected 1 blank line, found 0",
        "title_templated": False,
        "title": "Line is missing a blank line between the methods of a class.",
        "solution": "Add a blank line in between your class methods.",
        "explanation": ""
    },
    "E302": {
        "original_message": "expected 2 blank lines, found 0",
        "title_templated": False,
        "title": "Two blank lines are expected before and after each function or class.",
        "solution": "Ensure there are two blank lines before and after each function and class.",
        "explanation": ""
    },
    "E303": {
        "original_message": "too many blank lines (3)",
        "title_templated": False,
        "title": "Too many blank lines.",
        "solution": "Ensure there are only two blank lines between functions and classes and one blank line between methods of a class.",
        "explanation": ""
    },
    "E304": {
        "original_message": "blank lines found after function decorator",
        "title_templated": False,
        "title": "Line contains a blank line after a function decorator.",
        "solution": "Ensure that there are no blank lines between a function decorator and the function it is decorating.",
        "explanation": ""
    },
    "E305": {
        "original_message": "expected 2 blank lines after end of function or class",
        "title_templated": False,
        "title": "Functions and classes should have two blank lines after them.",
        "solution": "Ensure that functions and classes should have two blank lines after them.",
        "explanation": ""
    },
    "E306": {
        "original_message": "expected 1 blank line before a nested definition",
        "title_templated": False,
        "title": "Nested definitions should have one blank line before them.",
        "solution": "Ensure there is a blank line above your nested definition.",
        "explanation": ""
    },
    "E401": {
        "original_message": "multiple imports on one line",
        "title_templated": False,
        "title": "Line contains imports from different modules on the same line.",
        "solution": "Ensure import statements from different modules occur on their own line.",
        "explanation": ""
    },
    "E402": {
        "original_message": "module level import not at top of file",
        "title_templated": False,
        "title": "Module imports should be at the top of the file and there should be no statements in between module level imports.",
        "solution": "Ensure all import statements are at the top of the file and there are no statements in between imports.",
        "explanation": ""
    },
    "E501": {
        "original_message": "line too long (82 > 79 characters)",
        "title_templated": False,
        "title": "Line is longer than 79 characters.",
        "solution": "You should rewrite your long line of code by breaking it down across multiple lines.",
        "explanation": "By making sure your lines of code are not too complicated means it's easier to understand by other people. Also by limiting the line width makes it possible to have several files open side-by-side, and works well when using code review tools that present the two versions in adjacent columns."
    },
    "E502": {
        "original_message": "the backslash is redundant between brackets",
        "title_templated": False,
        "title": "There is no need for a backslash (`\\`) between brackets.",
        "solution": "Remove any backslashes between brackets.",
        "explanation": ""
    },
    "E701": {
        "original_message": "multiple statements on one line (colon)",
        "title_templated": False,
        "title": "Line contains multiple statements.",
        "solution": "Make sure that each statement is on its own line.",
        "explanation": "This improves readability."
    },
    "E702": {
        "original_message": "multiple statements on one line (semicolon)",
        "title_templated": False,
        "title": "Line contains multiple statements.",
        "solution": "Make sure that each statement is on its own line.",
        "explanation": "This improves readability of your code."
    },
    "E703": {
        "original_message": "statement ends with a semicolon",
        "title_templated": False,
        "title": "Line ends in a semicolon (`;`).",
        "solution": "Remove the semicolon from the end of the line, these are not used in Python 3.",
        "explanation": ""
    },
    # E704 ignored by default
    "E704": {
        "original_message": "multiple statements on one line (def)",
        "title_templated": False,
        "title": "Line contains multiple statements.",
        "solution": "Make sure multiple statements of a function definition are on their own separate lines.",
        "explanation": ""
    },
    "E711": {
        "original_message": "comparison to None should be ‘if cond is None:’",
        "title_templated": False,
        "title": "Comparisons to objects such as `True`, `False`, and `None` should use `is` or `is not` instead of `==` and `!=`.",
        "solution": "Replace `!=` with `is not` and `==` with `is`.",
        "explanation": "This makes your code easier to read, as it's using words rather than symbols."
    },
    "E712": {
        "original_message": "comparison to True should be ‘if cond is True:’ or ‘if cond:’",
        "title_templated": False,
        "title": "Comparisons to objects such as `True`, `False`, and `None` should use `is` or `is not` instead of `==` and `!=`.",
        "solution": "Replace `!=` with `is not` and `==` with `is`.",
        "explanation": "This makes your code easier to read, as it's using words rather than symbols."
    },
    "E713": {
        "original_message": "test for membership should be ‘not in’",
        "title_templated": False,
        "title": "When testing whether or not something is in an object use the form `x not in the_object` instead of `not x in the_object`.",
        "solution": "Use the form `not x in the_object` instead of `x not in the_object`.",
        "explanation": "This improves readability of your code as it reads more naturally."
    },
    "E714": {
        "original_message": "test for object identity should be ‘is not’",
        "title_templated": False,
        "title": "When testing for object identity use the form `x is not None` rather than `not x is None`.",
        "solution": "Use the form `x is not None` rather than `not x is None`.",
        "explanation": "This improves readability of your code as it reads more naturally."
    },
    "E721": {
        "original_message": "do not compare types, use ‘isinstance()’",
        "title_templated": False,
        "title": "You should compare an objects type by using `isinstance()` instead of `==`. This is because `isinstance` can handle subclasses as well.",
        "solution": "Use `if isinstance(dog, Animal)` instead of `if type(dog) == Animal`.",
        "explanation": ""
    },
    "E722": {
        "original_message": "do not use bare except, specify exception instead",
        "title_templated": False,
        "title": "Except block is calling all exceptions, instead it should catch a specific exception.",
        # TODO: Add a simple multi-except example
        "solution": "Add the specific exception the block is expected to catch, you may need to use multiple `except` blocks if you were catching multiple exceptions.",
        "explanation": "This helps other to know exactly what the `except` is expected to catch."
    },
    "E731": {
        "original_message": "do not assign a lambda expression, use a def",
        "title_templated": False,
        "title": "Line assigns a lambda expression instead of defining it as a function using `def`.",
        "solution": "Define the line as a function using `def`.",
        "explanation": "The primary reason for this is debugging. Lambdas show as `<lambda>` in tracebacks, where functions will display the function’s name."
    },
    "E741": {
        "original_message": "do not use variables named `l`, `O`, or `I`",
        "title_templated": False,
        "title": "Line uses one of the variables named `l`, `O`, or `I`",
        "solution": "Change the names of these variables to something more descriptive.",
        "explanation": "Variables named `l`, `O`, or `I` can be very hard to read. This is because the letter `I` and the letter `l` are easily confused, and the letter `O` and the number `0` can be easily confused."
    },
    "E742": {
        "original_message": "do not define classes named `l`, `O`, or `I`",
        "title_templated": False,
        "title": "Line contains a class named `l`, `O`, or `I`",
        "solution": "Change the names of these classes to something more descriptive.",
        "explanation": "Classes named `l`, `O`, or `I` can be very hard to read. This is because the letter `I` and the letter `l` are easily confused, and the letter `O` and the number `0` can be easily confused."
    },
    "E743": {
        "original_message": "do not define functions named `l`, `O`, or `I`",
        "title_templated": False,
        "title": "Line contains a function named `l`, `O`, or `I`",
        "solution": "Change the names of these functions to something more descriptive.",
        "explanation": "Functions named `l`, `O`, or `I` can be very hard to read. This is because the letter `I` and the letter `l` are easily confused, and the letter `O` and the number `0` can be easily confused."
    },
    "E999": {
        "original_message": "Syntax error",
        "title_templated": False,
        "title": "Program failed to compile.",
        "solution": "Make sure your code is working.",
        "explanation": ""
    },
    # TODO: Continue from this point onwards with checking text and adding templating boolean
    "W191": {
        "original_message": "indentation contains tabs",
        "title_templated": False,
        "title": "Line contains tabs when only spaces are expected.",
        "solution": "Replace any tabs in your indentation with spaces.",
        "explanation": "Using a consistent character for whitespace makes it much easier for editors to read your file."
    },
    "W291": {
        "original_message": "trailing whitespace",
        "title_templated": False,
        "title": "Line contains whitespace after the final character.",
        "solution": "Remove any extra whitespace at the end of each line.",
        "explanation": ""
    },
    "W292": {
        "original_message": "no newline at end of file",
        "title_templated": False,
        "title": "Files should end with a newline.",
        "solution": "Add a newline to the end of your file.",
        "explanation": "All text files should automatically end with a new line character, but some code editors can allow you to remove it."
    },
    "W293": {
        "original_message": "blank line contains whitespace",
        "title_templated": False,
        "title": "Blank lines should not contain any tabs or spaces.",
        "solution": "Remove any whitespace from blank lines.",
        "explanation": ""
    },
    "W391": {
        "original_message": "blank line at end of file",
        "title_templated": False,
        "title": "There are either zero, two, or more than two blank lines at the end of your file.",
        "solution": "Ensure there is only one blank line at the end of your file.",
        "explanation": ""
    },
    # W503 ignored by default
    # This seems contradicitng... https://lintlyci.github.io/Flake8Rules/rules/W503.html
    "W503": {
        "original_message": "line break before binary operator",
        "title_templated": False,
        "title": "Line break is before a binary operator.",
        "solution": "",
        "explanation": ""
    },
    # W504 ignored by default
    # same as above https://lintlyci.github.io/Flake8Rules/rules/W504.html
    "W504": {
        "original_message": "line break after binary operator",
        "title_templated": False,
        "title": "Line break is after a binary operator.",
        "solution": "",
        "explanation": ""
    },
    # W505 ignored by default
    "W505": {
        "original_message": "doc line too long (82 > 79 characters)",
        "title_templated": False,
        "title": "Line is longer than 79 characters.",
        "solution": "You should rewrite your long line of code by breaking it down across multiple lines.",
        "explanation": "By making sure your lines of code are not too complicated means it's easier to understand by other people. Also by limiting the line width makes it possible to have several files open side-by-side, and works well when using code review tools that present the two versions in adjacent columns."
    },
    "W601": {
        "original_message": ".has_key() is deprecated, use ‘in’",
        "title_templated": False,
        "title": "`.has_key()` was deprecated in Python 2. It is recommended to use the `in` operator instead.",
        "solution": """
Use `in` instead of `.has_key()`.

For example:

```
if 8054 in postcodes:
```
""",
        "explanation": ""
    },
    "W602": {
        "original_message": "deprecated form of raising exception",
        "title_templated": False,
        "title": "Using `raise ExceptionType, message` is not supported.",
        "solution": "Instead of using `raise ExceptionType, 'Error message'`, passing the text as a parameter to the exception, like `raise ExceptionType('Error message')`.",
        "explanation": ""
    },
    "W603": {
        "original_message": "‘<>’ is deprecated, use ‘!=’",
        "title_templated": False,
        "title": "`<>` has been removed in Python 3.",
        "solution": "Replace any occurences of `<>` with `!=`.",
        "explanation": "The `!=` is the common programming symbols for stating not equal."
    },
    "W604": {
        "original_message": "backticks are deprecated, use ‘repr()’",
        "title_templated": False,
        "title": "Backticks have been removed in Python 3.",
        "solution": "Use the built-in function `repr()` instead.",
        "explanation": ""
    },
    "W605": {
        "original_message": "invalid escape sequence ‘x’",
        "title_templated": False,
        "title": "Backslash is used to escape a character that cannot be escaped.",
        "solution": "Either don't use the backslash, or check your string is correct.",
        "explanation": ""
    },
    "W606": {
        "original_message": "`async` and `await` are reserved keywords starting with Python 3.7",
        "title_templated": False,
        "title": "`async` and `await` are reserved names",
        "solution": "Do not name variables or functions as `async` or `await`.",
        "explanation": ""
    },
    "D100": {
        "original_message": "Missing docstring in public module",
        "title_templated": False,
        "title": "Module (the term for the Python file) should have a docstring.",
        "solution": "Add a docstring to your module.",
        "explanation": """
A docstring is a special comment at the top of your module that briefly explains the purpose of the module. It should have 3 sets of quotes to start and finish the comment.

For example:

```
\"\"\"This file calculates required dietary requirements for kiwis.
```
"""
    },
    "D101": {
        "original_message": "Missing docstring in public class",
        "title_templated": False,
        "title": "Class should have a docstring.",
        "solution": "Add a docstring to your class.",
        "explanation": """
A docstring is a special comment at the top of your class that briefly explains the purpose of the class. It should have 3 sets of quotes to start and finish the comment.

For example:

```
class Kiwi():
    \"\"\"Represents a kiwi bird from New Zealand.\"\"\"
```
"""
    },
    "D102": {
        "original_message": "Missing docstring in public method",
        "title_templated": False,
        "title": "Methods should have docstrings.",
        "solution": "Add a docstring to your method.",
        "explanation": """
A docstring is a special comment at the top of your method that briefly explains the purpose of the method. It should have 3 sets of quotes to start and finish the comment.

For example:

```
class Kiwi():
    \"\"\"Represents a kiwi bird from New Zealand.\"\"\"

    def eat_plants(amount):
        \"\"\"Calculates calories from the given amount of plant food and eats it.\"\"\"
```
"""
    },
    "D103": {
        "original_message": "Missing docstring in public function",
        "title_templated": False,
        "title": "This function should have a docstring.",
        "solution": "Add a docstring to your function.",
        "explanation": """
A docstring is a special comment at the top of your module that briefly explains the purpose of the function. It should have 3 sets of quotes to start and finish the comment.

For example:

```
def get_waypoint_latlng(number):
    \"\"\"Return the latitude and longitude values of the waypoint.\"\"\"
```
"""
    },
    "D104": {
        "original_message": "Missing docstring in public package",
        "title_templated": False,
        "title": "Packages should have docstrings.",
        "solution": "Add a docstring to your package.",
        "explanation": ""
    },
    "D105": {
        "original_message": "Missing docstring in magic method",
        "title_templated": False,
        "title": "Magic methods should have docstrings.",
        "solution": "Add a docstring to your magic method.",
        "explanation": ""
    },
    "D106": {
        "original_message": "Missing docstring in public nested class",
        "title_templated": False,
        "title": "Public nested classes should have docstrings.",
        "solution": "Add a docstring to your public nested class.",
        "explanation": ""
    },
    "D107": {
        "original_message": "Missing docstring in __init__",
        "title_templated": False,
        "title": "The `__init__` method should have a docstring.",
        "solution": "Add a docstring to your `__init__` method.",
        "explanation": "This helps understand how objects of your class are created."
    },
    "D200": {
        "original_message": "One-line docstring should fit on one line with quotes",
        "title_templated": False,
        "title": "Docstrings that are one line long should fit on one line with quotes.",
        "solution": "Put your docstring on one line with quotes.",
        "explanation": ""
    },
    "D201": {
        "original_message": "No blank lines allowed before function docstring",
        "title_templated": False,
        "title": "Function docstrings should not have blank lines before them.",
        "solution": "Remove any blank lines before your function docstring.",
        "explanation": ""
    },
    "D202": {
        "original_message": "No blank lines allowed after function docstring",
        "title_templated": False,
        "title": "Function docstrings should not have blank lines after them.",
        "solution": "Remove any blank lines after your function docstring.",
        "explanation": ""
    },
    "D203": {
        "original_message": "1 blank line required before class docstring",
        "title_templated": False,
        "title": "Class docstrings should have 1 blank line before them.",
        "solution": "Insert 1 blank line before your class docstring.",
        "explanation": ""
    },
    "D204": {
        "original_message": "1 blank line required after class docstring",
        "title_templated": False,
        "title": "Class docstrings should have 1 blank line after them.",
        "solution": "Insert 1 blank line after your class docstring.",
        "explanation": "This improves the readability of your code."
    },
    "D205": {
        "original_message": "1 blank line required between summary line and description",
        "title_templated": False,
        "title": "There should be 1 blank line between the summary line and the description.",
        "solution": "Insert 1 blank line between the summary line and the description.",
        "explanation": """
This makes larger docstrings easier to read.

For example:

```
def get_stock_level(book):
    \"\"\"Return the stock level for the given book.

    This calculates the stock level across multiple stores in the city,
    excluding books reserved for customers.

    Args:
        book (str): Name of the book.

    Returns:
        String of publication date in the format of 'DD/MM/YYYY'.
    \"\"\"
```
"""
    },
    "D206": {
        "original_message": "Docstring should be indented with spaces, not tabs",
        "title_templated": False,
        "title": "Docstrings should be indented using spaces, not tabs.",
        "solution": "Make sure your docstrings are indented using spaces instead of tabs.",
        "explanation": ""
    },
    "D207": {
        "original_message": "Docstring is under-indented",
        "title_templated": False,
        "title": "Docstring is under-indented.",
        "solution": "Add indentation levels to your docstring until it is at the correct indentation level.",
        "explanation": ""
    },
    "D208": {
        "original_message": "Docstring is over-indented",
        "title_templated": False,
        "title": "Docstring is over-indented.",
        "solution": "Remove indentation levels from your docstring until it is at the correct indentation level.",
        "explanation": ""
    },
    "D209": {
        "original_message": "Multi-line docstring closing quotes should be on a separate line",
        "title_templated": False,
        "title": "Docstrings that are longer than one line should have closing quotes on a separate line.",
        "solution": "Put the closing quotes of your docstring on a separate line.",
        "explanation": """
This makes larger docstrings easier to read.

For example:

```
def get_stock_level(book):
    \"\"\"Return the stock level for the given book.

    This calculates the stock level across multiple stores in the city,
    excluding books reserved for customers.

    Args:
        book (str): Name of the book.

    Returns:
        String of publication date in the format of 'DD/MM/YYYY'.
    \"\"\"
```
"""
    },
    "D210": {
        "original_message": "No whitespaces allowed surrounding docstring text",
        "title_templated": False,
        "title": "Text in docstrings should not be surrounded by whitespace.",
        "solution": "Remove any whitespace from the start and end of your docstring.",
        "explanation": ""
    },
    "D211": {
        "original_message": "No blank lines allowed before class docstring",
        "title_templated": False,
        "title": "Class docstrings should not have blank lines before them.",
        "solution": "Remove any blank lines before your class docstring.",
        "explanation": ""
    },
    "D212": {
        "original_message": "Multi-line docstring summary should start at the first line",
        "title_templated": False,
        "title": "Docstrings that are more than one line long should start at the first line.",
        "solution": """
Ensure your docstring starts on the first line with quotes.

For example:

```
def get_stock_level(book):
    \"\"\"Return the stock level for the given book.
```
""",
        "explanation": ""
    },
    "D213": {
        "original_message": "Multi-line docstring summary should start at the second line",
        "title_templated": False,
        "title": "Docstrings that are more than one line long should start at the second line.",
        "solution": "Ensure your docstring starts on the second line, which is the first line without quotes.",
        "explanation": ""
    },
    "D214": {
        "original_message": "Section is over-indented",
        "title_templated": False,
        "title": "Section is indented by too many levels.",
        "solution": "Remove indentation levels from this section until it is at the correct indentation level.",
        "explanation": ""
    },
    "D215": {
        "original_message": "Section underline is over-indented",
        "title_templated": False,
        "title": "Section underline is indented by too many levels.",
        "solution": "Remove indentation levels from this section underline until it is at the correct indentation level.",
        "explanation": ""
    },
    "D300": {
        "original_message": "Use \"\"\"triple double quotes\"\"\"",
        "title_templated": False,
        "title": "Use \"\"\"triple double quotes\"\"\" around docstrings.",
        "solution": "Use \"\"\" triple double quotes around your docstring.",
        "explanation": ""
    },
    "D301": {
        "original_message": "Use r\"\"\" if any backslashes in a docstring",
        "title_templated": False,
        "title": "Use r\"\"\" if there are any backslashes in a docstring.",
        "solution": "Use r\"\"\" at the beginning of your docstring if it contains any backslashes.",
        "explanation": ""
    },
    "D302": {
        "original_message": "Use u\"\"\" for Unicode docstrings",
        "title_templated": False,
        "title": "Use u\"\"\" for docstrings that contain Unicode.",
        "solution": "Use u\"\"\" at the beginning of your docstring if it contains any Unicode.",
        "explanation": ""
    },
    "D400": {
        "original_message": "First line should end with a period",
        "title_templated": False,
        "title": "The first line in docstrings should end with a period.",
        "solution": "Add a period to the end of the first line in your docstring. It should be a short summary of your code, if it's too long you may need to break it apart into multiple sentences.",
        "explanation": ""
    },
    "D401": {
        "original_message": "First line should be in imperative mood",
        "title_templated": False,
        "title": "The first line in docstrings should read like a command.",
        "solution": "Ensure the first line in your docstring reads like a command, not a description. For example 'Do this' instead of 'Does this', 'Return this' instead of 'Returns this'.",
        "explanation": ""
    },
    "D402": {
        "original_message": "First line should not be the function’s signature",
        "title_templated": False,
        "title": "The first line in docstrings should not be a copy of the function’s definition.",
        "solution": "Rewrite the docstring to describe the purpose of the function.",
        "explanation": ""
    },
    "D403": {
        "original_message": "First word of the first line should be properly capitalized",
        "title_templated": False,
        "title": "The first word in the first line should be capitalised.",
        "solution": "Capitalise the first word.",
        "explanation": ""
    },
    "D404": {
        "original_message": "First word of the docstring should not be 'This'",
        "title_templated": False,
        "title": "First word of the docstring should not be 'This'.",
        "solution": "Rephrase the docstring so that the first word is not 'This'.",
        "explanation": ""
    },
    "D405": {
        "original_message": "Section name should be properly capitalized",
        "title_templated": False,
        "title": "Section name should be properly capitalised.",
        "solution": "Capitalise the section name.",
        "explanation": ""
    },
    "D406": {
        "original_message": "Section name should end with a newline",
        "title_templated": False,
        "title": "Section names should end with a newline.",
        "solution": "Add a newline after the section name.",
        "explanation": ""
    },
    "D407": {
        "original_message": "Missing dashed underline after section",
        "title_templated": False,
        "title": "Section names should have a dashed line underneath them.",
        "solution": "Add a dashed line underneath the section name.",
        "explanation": ""
    },
    "D408": {
        "original_message": "Section underline should be in the line following the section’s name",
        "title_templated": False,
        "title": "Dashed line should be on the line following the section's name.",
        "solution": "Put the dashed underline on the line immediately following the section name.",
        "explanation": ""
    },
    "D409": {
        "original_message": "Section underline should match the length of its name",
        "title_templated": False,
        "title": "Dashed section underline should match the length of the section's name.",
        "solution": "Add or remove dashes from the dashed underline until it matches the length of the section name.",
        "explanation": ""
    },
    "D410": {
        "original_message": "Missing blank line after section",
        "title_templated": False,
        "title": "Section should have a blank line after it.",
        "solution": "Add a blank line after the section.",
        "explanation": ""
    },
    "D411": {
        "original_message": "Missing blank line before section",
        "title_templated": False,
        "title": "Section should have a blank line before it.",
        "solution": "Add a blank line before the section.",
        "explanation": ""
    },
    "D412": {
        "original_message": "No blank lines allowed between a section header and its content",
        "title_templated": False,
        "title": "There should be no blank lines between a section header and its content.",
        "solution": "Remove any blank lines that are between the section header and its content.",
        "explanation": ""
    },
    "D413": {
        "original_message": "Missing blank line after last section",
        "title_templated": False,
        "title": "The last section in a docstring should have a blank line after it.",
        "solution": "Add a blank line after the last section in your docstring.",
        "explanation": ""
    },
    "D414": {
        "original_message": "Section has no content",
        "title_templated": False,
        "title": "Sections in docstrings must have content.",
        "solution": "Add content to the section in your docstring.",
        "explanation": ""
    },
    "D415": {
        "original_message": "First line should end with a period, question mark, or exclamation point",
        "title_templated": False,
        "title": "The first line in your docstring should end with a period, question mark, or exclamation point.",
        "solution": "Add a period, question mark, or exclamation point to the end of the first line in your docstring.",
        "explanation": ""
    },
    "D416": {
        "original_message": "Section name should end with a colon",
        "title_templated": False,
        "title": "Section names should end with a colon.",
        "solution": "Add a colon to the end of your section name.",
        "explanation": ""
    },
    "D417": {
        "original_message": "Missing argument descriptions in the docstring",
        "title_templated": False,
        "title": "Docstrings should include argument descriptions.",
        "solution": "Add argument descriptions to your docstring.",
        "explanation": ""
    },
    "N801": {
        "original_message": "class names should use CapWords convention",
        "title_templated": False,
        "title": "Class names should use the CapWords convention.",
        "solution": "Edit your class names to follow the CapWords convention, where each word is capitalised with no spaces.",
        "explanation": ""
    },
    "N802": {
        "original_message": "function name should be lowercase",
        "title_templated": False,
        "title": "Function names should be lowercase.",
        "solution": "Edit your function names to be lowercase, with underscores for spaces.",
        "explanation": ""
    },
    "N803": {
        "original_message": "argument name should be lowercase",
        "title_templated": False,
        "title": "Argument names should be lowercase.",
        "solution": "Edit your function names to be lowercase, with underscores for spaces.",
        "explanation": ""
    },
    "N804": {
        "original_message": "first argument of a classmethod should be named `cls`",
        "title_templated": False,
        "title": "The first argument of a classmethod should be named `cls`.",
        "solution": "Edit the first argument in your classmethod to be named `cls`.",
        "explanation": "This is the common term that Python programmers use for a classmethod."
    },
    "N805": {
        "original_message": "first argument of a method should be named `self`",
        "title_templated": False,
        "title": "The first argument of a method should be named `self`.",
        "solution": "Edit the first argument in your method to be named `self`.",
        "explanation": "This is the common term that Python programmers use for the object of a class's method."
    },
    "N806": {
        "original_message": "variable in function should be lowercase",
        "title_templated": False,
        "title": "Variables in functions should be lowercase.",
        "solution": "Edit the variable in your function to be lowercase.",
        "explanation": ""
    },
    "N807": {
        "original_message": "function name should not start and end with `__`",
        "title_templated": False,
        "title": "Function names should not start and end with `__` (double underscore).",
        "solution": "Edit the function name so that it does not start and end with `__`",
        "explanation": ""
    },
    "N811": {
        "original_message": "constant imported as non constant",
        "title_templated": False,
        "title": "Import that should have been imported as a constant has been imported as a non constant.",
        "solution": "Edit the import to be imported as a constant (use all capital letters in the 'import as...' name).",
        "explanation": ""
    },
    "N812": {
        "original_message": "lowercase imported as non lowercase",
        "title_templated": False,
        "title": "Import that should have been imported as lowercase has been imported as non lowercase",
        "solution": "Edit the import to be imported as lowercase (use lowercase in the `import as` name).",
        "explanation": ""
    },
    "N813": {
        "original_message": "camelcase imported as lowercase",
        "title_templated": False,
        "title": "Import that should have been imported as camelCase has been imported as lowercase.",
        "solution": "Edit the import to be imported as camelCase (use camelCase in the 'import as ...' name).",
        "explanation": ""
    },
    "N814": {
        "original_message": "camelcase imported as constant",
        "title_templated": False,
        "title": "Import that should have been imported as camelCase has been imported as a constant.",
        "solution": "Edit the import to be imported as camelCase (use camelCase in the 'import as ...' name).",
        "explanation": ""
    },
    "N815": {
        "original_message": "mixedCase variable in class scope",
        "title_templated": False,
        "title": "Mixed case variable used in the class scope",
        "solution": "Edit the variable name so that it doesn't use mixedCase.",
        "explanation": ""
    },
    "N816": {
        "original_message": "mixedCase variable in global scope",
        "title_templated": False,
        "title": "Mixed case variable used in the global scope",
        "solution": "Edit the variable name so that it doesn't use mixedCase.",
        "explanation": ""
    },
    "N817": {
        "original_message": "camelcase imported as acronym",
        "title_templated": False,
        "title": "Import that should have been imported as camelCase has been imported as an acronym.",
        "solution": "Edit the import to be imported as camelCase (use camelCase in the 'import as...' name).",
        "explanation": ""
    },
    "Q000": {
        "original_message": "Remove bad quotes",
        "title_templated": False,
        "title": "Use single quotes (') instead of double quotes (\").",
        "solution": "Replace any double quotes with single quotes.",
        "explanation": ""
    },
    "Q001": {
        "original_message": "Remove bad quotes from multiline string",
        "title_templated": False,
        "title": "Use single quotes (') instead of double quotes (\") in multiline strings.",
        "solution": "Replace any double quotes in your multiline string with single quotes.",
        "explanation": ""
    },
    "Q002": {
        "original_message": "Remove bad quotes from docstring",
        "title_templated": False,
        "title": "Use single quotes (') instead of double quotes (\") in docstrings.",
        "solution": "Replace any double quotes in your docstring with single quotes.",
        "explanation": ""
    },
    "Q003": {
        "original_message": "Change outer quotes to avoid escaping inner quotes",
        "title_templated": False,
        "title": "Change outer quotes to avoid escaping inner quotes.",
        "solution": "Make either the outer quotes single (`'`) and the inner quotes double (`\"`), or the outer quotes double and the inner quotes single.",
        "explanation": ""
    },
}
