# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# <div style="text-align:center; font-size:200%;">
#  <b>Piraten-Beute</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Piraten-Beute.py -->
# <!-- python_courses/slides/projects/project_100_pirate_loot.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Piraten-Beute
#
# Da die Automatisierung der Beuteaufteilung für Ihre Piraten-Bande sehr
# erfolgreich war, wollen Sie jetzt auch das Melden der Beute automatisieren.
#
# Schreiben Sie dazu eine Funktion `found_loot(what: str, value: int) -> str`, die
# einen Bericht zurückgibt:
#
# ```python
# >>> create_loot_report("old fishing net", 0)
# 'Found an old fishing net. Its worth seems to be nothing, Zounds!!!'
# >>> create_loot_report("pile of firewood", 1)
# 'Found a pile of firewood. Its worth seems to be a single, darned doubloon!'
# >>> create_loot_report("diamond ring", 100)
# 'Found a diamond ring. Its worth seems to be 100 doubloons.'
# ```
#
# Beachten Sie, dass der Artikel (`a` oder `an`) davon abhängt, ob `what` mit einem
# Vokal oder Konsonant anfängt und der Text für die Höhe der Beute für 0, 1 und mehr
# Golddublonen verschieden ist.


# %% tags=["alt"]
def article_for(word: str) -> str:
    if word[0] in "aeiou":
        return "an"
    else:
        return "a"


# %% tags=["alt"]
def value_phrase(doubloons: int) -> str:
    if doubloons == 0:
        return "nothing, Zounds!!!"
    elif doubloons == 1:
        return "a single, darned doubloon!"
    else:
        return f"{doubloons} doubloons."


# %%
def create_loot_report(what: str, value: int) -> str:
    return (
        f"Found {article_for(what)} {what}. "
        f"Its worth seems to be {value_phrase(value)}"
    )


# %% tags=["keep"]
assert (
    create_loot_report("old fishing net", 0)
    == "Found an old fishing net. Its worth seems to be nothing, Zounds!!!"
)

# %% tags=["keep"]
assert (
    create_loot_report("pile of firewood", 1)
    == "Found a pile of firewood. Its worth seems to be a single, darned doubloon!"
)

# %% tags=["keep"]
assert (
    create_loot_report("diamond ring", 100)
    == "Found a diamond ring. Its worth seems to be 100 doubloons."
)
