# intellij-auto-import-does-not-include-source-root
Repository with minimal reproducible code for https://youtrack.jetbrains.com/issue/PY-14206

This is a showcase of the package using [flat layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#flat-layout).

It's purpose is to show that in IntelliJ PyCharm/IDEA the autoimport assumes the [src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout)
and ignores the package name in case of different repository structure.

# Reproducing the bug
 * Checkout the repo
 * Open /app/main.py 
 * Remove the line with import
 * Apply the autoimport suggestion for HelloWorldPrinter
 * You will see that the auto-import applied the 'from lib.hello import HelloWorldPrinter' instead of 'from app.lib.hello import HelloWorldPrinter'
