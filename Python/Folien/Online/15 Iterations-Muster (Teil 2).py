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
#  <b>Iterations-Muster (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 Iterations-Muster (Teil 2).py -->
# <!-- python_courses/slides/module_150_collections/topic_158_b3_iteration_patterns2.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Transformation von Listen

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %% [markdown] lang="de"
# ## Mini-Workshop: Quadratzahlen
#
# Gegeben sei die folgende Liste mit Zahlen.

# %% lang="de" tags=["keep"]
zahlen = [1, 7, 4, 87, 23]

# %% [markdown] lang="de"
# Erzeugen Sie eine neue Liste, die die Quadrate der Zahlen in `numbers` enthält.

# %% lang="de"
ergebnis = []
for n in zahlen:
    ergebnis.append(n * n)
ergebnis


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die eine neue Liste mit den
# Quadraten der Zahlen in `zahlen` zurückgibt.

# %% lang="de"
def quadriere(zahlen):
    ergebnis = []
    for n in zahlen:
        ergebnis.append(n * n)
    return ergebnis


# %% lang="de"
assert quadriere(zahlen) == [1, 49, 16, 7569, 529]
