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
#  <b>Komprehensionen: Elegantere Iteration</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 17 Komprehensionen Elegantere Iteration.py -->
# <!-- python_courses/slides/module_150_collections/topic_200_a4_comprehension.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Eleganter: Listen-Komprehension

# %% tags=["keep"]
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ## Mini-Workshop
#
# Schreiben Sie die folgenden Ausdrücke als Listen-Komprehensionen:

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result

# %%


# %% [markdown] lang="de"
# # Quadratzahlen mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste mit den Quadraten von `numbers`. Verwenden Sie
# dazu eine Listen-Komprehension

# %% tags=["keep"]
numbers = [1, 7, 4, 87, 23]

# %%


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die jedes Element einer Liste
# quadriert, mit Listen-Komprehension.

# %%

# %%


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result


# %%


# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Tupledatenbank
#
# Wir haben eine Tupeldatenbank mit den folgenden Einträgen:
#
# ```python
# data = [
#     ("Max", "Mustermann", 1999, "Musterstadt"),
#     ("John", "Doe", 1995, "New York"),
#     ("Jane", "Doe", 1996, "New York"),
#     ("Erika", "Mustermann", 2002, "Musterstadt"),
#     ("Franziska", "Musterfrau", 2001, "Musterstadt"),
#     ("Max", "Mustermann", 1972, "Musterstadt"),
#     ("Max", "Power", 1972, "Springfield"),
#     ("Peter", "Pan", 1953, "Nimmerland"),
# ]
# ```
#
# Schreiben Sie eine Funktion `filter_city(data, city)`, die eine Liste
# aller Personen zurückgibt, die in der Stadt `city` leben. Verwenden Sie 
# dazu eine list comprehension. Die Liste soll dabei aus Tupeln der Form `(Vorname, Nachname)` bestehen.
#

# %% tags=["keep"]
data = [
    ("Max", "Mustermann", 1999, "Musterstadt"),
    ("John", "Doe", 1995, "New York"),
    ("Jane", "Doe", 1996, "New York"),
    ("Erika", "Mustermann", 2002, "Musterstadt"),
    ("Franziska", "Musterfrau", 2001, "Musterstadt"),
    ("Max", "Mustermann", 1972, "Musterstadt"),
    ("Max", "Power", 1972, "Springfield"),
    ("Peter", "Pan", 1953, "Nimmerland"),
]

# %%

# %%


# %% [markdown] lang="de"
# # Filtern mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält, die größer
# als 10 sind. Verwenden Sie dazu Listen-Komprehension.

# %%


# %% [markdown] lang="de"
# Schreiben Sie die Funktion `zahlen_größer_als_10(zahlen)` mit
# Listen-Komprehension.

# %%

# %%
