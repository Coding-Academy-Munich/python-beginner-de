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
#  <b>Aufzählen von Elementen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 19 Aufzählen von Elementen.py -->
# <!-- python_courses/slides/module_150_collections/topic_156_enumerate.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Aufzählen von Elementen
#
# In manchen Fällen ist es hilfreich, bei der Iteration über eine Liste
# sowohl den Index des aktuellen Elements, als auch das Element selber
# zur Verfügung zu haben.
#
# Ein Beispiel dafür ist die bereits besprochene `find()` Funktion.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Nochmal Finden von Elementen
#
# Bei unserer bisherigen Version von `find` muss die Liste zweimal durchlaufen
# werden:
#
# - Einmal um zu testen, ob das gesuchte Element in der Liste vorkommt
# - Einmal um den Index zu finden.
#
# Schöner wäre es, wenn wir das in einem Durchlauf erledigen könnten.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Funktion `enumerate()` nimmt eine Liste als Argument und liefert
# ein Iterable bestehend aus Paaren `(index, element)` zurück:

# %% tags=["keep"]
my_list = ["a", "b", "c", "d", "e"]

# %%
enumerate(my_list)

# %%
list(enumerate(my_list))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
for index, element in enumerate(my_list):
    print(f"index = {index}, element = {element}")

# %%
for pos, element in enumerate(my_list, 1):
    print(f"Pos = {pos}, element = {element}")


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def find(element, a_list):
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            return index
    return None


# %% tags=["alt"]
def find(element, a_list):
    result = None
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            result = index
            break
    return result


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
my_list = ["a", "b", "c", "d", "a"]

# %%
find("a", my_list)

# %%
find("d", my_list)

# %%
find("x", my_list)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
assert find("a", my_list) == 0
assert find("d", my_list) == 3
assert find("x", my_list) is None


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Finden des letzten Elements
#
# Schreiben Sie eine Funktion `find_last(element, a_list: list)`, die den Index des
# *letzten* Vorkommens von `element` in `a_list` zurückgibt, oder `None` falls das
# Element nicht in der Liste vorkommt.


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Mögliches Vorgehen
#
# - Laufe durch alle Elemente der Liste
# - Wenn das aktuelle Element gleich dem gesuchten Element ist, speichere den Index
# - Nachdem alle Elemente durchlaufen wurden: Gib den gespeicherten Index zurück
# - (Oder None, wenn kein Index gefunden wurde)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def find_last(element, a_list: list):
    last_index = None
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            last_index = index
    return last_index


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
values = [1, 3, 2, 3, 1, 1]

# %% tags=["keep"]
assert find_last(1, values) == 5
assert find_last(2, values) == 2
assert find_last(3, values) == 3
assert find_last(4, values) is None


# %% tags=["alt"]
def find_last_rev(element, a_list: list):
    for back_offset, list_entry in enumerate(reversed(a_list), 1):
        if list_entry == element:
            return len(a_list) - back_offset
    return None


# %% tags=["alt"]
assert find_last_rev(1, values) == 5
assert find_last_rev(2, values) == 2
assert find_last_rev(3, values) == 3
assert find_last_rev(4, values) is None
