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
#  <b>Iteration über Dictionaries</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Iteration über Dictionaries.py -->
# <!-- python_courses/slides/module_150_collections/topic_162_a1_iteration_over_dicts.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Iteration über Schlüssel

# %% tags=["keep"]
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Iteration über Werte

# %% tags=["keep"]
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Iteration über Key-Value-Paare

# %% tags=["keep"]
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Drucken von Lagerbeständen
#
# Wir schreiben die Software für ein Hochregallager, in dem der Lagerbestand in einem
# Dictionary verwaltet wird.
#
# Die Keys im Dictionary sind die Plätze im Lager, die Werte das am jeweiligen Platz
# gespeicherte Produkt.
#
# Schreiben Sie die folgenden Funktionen:
#
# - `print_inventory(warehouse)`, die alle im Lager vorhandenen Produkte ausdruckt
# - `print_locations(warehouse)`, die alle Plätze im Lager ausdruckt
# - `print_assignments(warehouse)`, die für jedes Produkt ausgibt, in welchem
#    Platz es gespeichert ist.


# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ```python
# >>> my_warehouse = {(0, 0): "plugs", (1, 0): "cables", (0, 1): "circuit boards"}
# ```
#
# ```python
# >>> print_inventory(my_warehouse)
# plugs
# cables
# circuit boards
# ```
#
# ```python
# >>> print_locations(my_warehouse)
# (0, 0)
# (1, 0)
# (0, 1)
# ```
#
# ```python
# >>> print_assignments(my_warehouse)
# plugs          -> (0, 0)
# cables         -> (1, 0)
# circuit boards -> (0, 1)
# ```


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
my_warehouse = {(0, 0): "plugs", (1, 0): "cables", (0, 1): "circuit boards"}

# %%

# %% tags=["keep"]
print_inventory(my_warehouse)

# %%

# %%%% tags=["keep"]
print_locations(my_warehouse)

# %%

# %%%% tags=["keep"]
print_assignments(my_warehouse)
