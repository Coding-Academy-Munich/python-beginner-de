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
#  <b>Iterations-Muster (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 16 Iterations-Muster (Teil 3).py -->
# <!-- python_courses/slides/module_150_collections/topic_159_b3_iteration_patterns3.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Filtern von Listen

# %% lang="de"
ergebnis = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        ergebnis.append(item)
ergebnis

# %% lang="de"
ergebnis = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if "ab" in item:
        ergebnis.append(item)
ergebnis

# %% [markdown] lang="de"
# # Mini-Workshop: Filtern von Listen
#
# Gegeben sei die folgende Liste mit Zahlen:

# %% lang="de" tags=["keep"]
zahlen = [1, 183, 7, 4, 87, 10, 23, -12, 493, 11]

# %% [markdown] lang="de"
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält,
# die größer als 10 sind.

# %% lang="de"
ergebnis = []
for n in zahlen:
    if n > 10:
        ergebnis.append(n)
ergebnis


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `zahlen_größer_als_10(zahlen)`, die eine neue
# Liste zurückgibt, die die Zahlen aus `zahlen` enthält, die größer als 10 sind.

# %% lang="de"
def zahlen_größer_als_10(zahlen):
    result = []
    for n in zahlen:
        if n > 10:
            result.append(n)
    return result


# %% lang="de"
assert zahlen_größer_als_10(zahlen) == [183, 87, 23, 493, 11]
