1. Which issues were the easiest to fix, and which were the hardest? Why?
Ans:
Easiest: The easiest issues were the simple style violations flagged like 'unused import' and 'trailing whitespaces'. 
They were simple to fix because the solution was direct, unambiguous and didn't require any logical changes to the program.

Hardest: The most "difficult" issue was the 'dangerous-default-value' warning for logs=[] in the addItem function. 
This was hard to fix as it's a bug that doesn't cause a syntax error, but rather incorrect program behavior over time. 
Understanding why a mutable default argument is a problem as it's shared across all calls, was much harder than just fixing a whitespace error.

2. Did the static analysis tools report any false positives? If so, describe one example.
Ans:
The 'Using the global statement' warning from Pylint could be considered a "pragmatic" false positive. While using globals is indeed bad practice in 
large applications, it's a perfectly understandable and functional choice for a simple script like this. The "perfect" fix would involve a major refactor to pass 
the stock_data dictionary as a parameter to every single function, which is overly complex for this lab's scope. We ultimately "fixed" it by 
adding a pylint: disable comment, acknowledging the warning without refactoring the entire program.

4. How would you integrate static analysis tools into your actual software development
workflow? Consider continuous integration (CI) or local development practices.
Ans:
I would integrate these tools at two key points:
Local Development: I would install them as extensions directly in my code editor (like VS Code). This provides real-time "linting," underlining errors and style 
issues as I type. This allows me to fix problems immediately, which is far more efficient than waiting for a later report.

Continuous Integration (CI): I would configure a CI pipeline (e.g., using GitHub Actions) to automatically run pylint, flake8, and bandit as a required check 
for every pull request. This acts as a "quality gate," ensuring that no code with critical security vulnerabilities, bugs, or major style violations can be merged into the main codebase.

4. What tangible improvements did you observe in the code quality, readability, or potential
robustness after applying the fixes?
Ans:
The code quality improved in three major ways:
Robustness: The program is far less likely to crash or behave unexpectedly. Fixing the dangerous-default-value bug ensures the logs will be correct. Replacing the bare except
with except KeyError in remove_item means the program will no longer ignore critical errors (like a KeyboardInterrupt). Using with open() for file I/O prevents resource leaks.

Security: The most critical improvement was removing the eval() call. This eliminated a high-confidence, medium-severity security vulnerability that could have allowed for remote code execution.

Readability: The code is significantly cleaner. By adding docstrings, fixing function names to snake_case, and correcting all whitespace issues, the code is now self-documenting 
and adheres to the standard PEP 8 style guide. This makes it much easier for any other Python developer to read, understand, and maintain.

