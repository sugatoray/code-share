# 🔥 USE the regex module (re) to split text into words
#    👉 You can also use regex patterns for a much
#       effective splitting.
#    👉 Use re.split("pattern", "text")
#
# 💡 Regex Patterns: Examples
#    👉 " |-|_" is the same as saying " " OR "-" OR "_"
#    👉 "\s[-_]" also means the same pattern as " -_"
# -----------------------------------------------------

import re

text = "This is a jam-packed fun concert called Under_Scored"

re.split(" |-|_", text) # pattern-1
# ['This', 'is', 'a', 'jam', 'packed', 'fun', 'concert', 'called', 'Under', 'Scored']

re.split("\s[-_]", text) # pattern-2
# ['This', 'is', 'a', 'jam', 'packed', 'fun', 'concert', 'called', 'Under', 'Scored']
