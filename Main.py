# Initial Commit

import pygbif as bgif
from pygbif import registry
from pygbif import species

suggest = species.name_suggest(q="Blue bird")

print(suggest)