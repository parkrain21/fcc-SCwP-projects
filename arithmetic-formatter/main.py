# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

print(repr(arithmetic_arranger(["1 + 2", "1 - 9380"])))
print(arithmetic_arranger(["3214 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
# main()
