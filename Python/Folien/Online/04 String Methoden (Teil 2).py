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
#  <b>String Methoden (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 String Methoden (Teil 2).py -->
# <!-- python_courses/slides/module_120_data_types/topic_190_a3_string_methods_part2.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # String Methoden (Teil 2)
#
# Mit der `join()` Methode können mehrere Strings mit einem Trennzeichen (oder
# Trenn-String) zusammengefügt werden:

# %% lang="de"
" ".join(["das", "sind", "mehrere", "strings"])

# %% lang="de"
", ".join(["Pferd", "Katze", "Hund"])

# %%
"".join(["ab", "cde", "f"])


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Aufzählung
#
# Schreiben Sie eine Funktion `enumerate_items(items: list[str]) -> list[str]`,
# die jeden Eintrag in einer Liste von Strings folgendermaßen umwandelt:
#
# ```python
# >>> enumerate_items(["Kaufe Semmeln", "Koche Kaffee", "Frühstücke"])
# ['1. Kaufe Semmeln', '2. Koche Kaffee', '3. Frühstücke']
# ```


# %%
def enumerate_items(items: list[str]) -> list[str]:
    result = []
    for index, item in enumerate(items, 1):
        result.append(f"{index}. {item}")
    return result


# %% lang="de" tags=["keep"]
assert enumerate_items(["Kaufe Semmeln", "Koche Kaffee", "Frühstücke"]) == [
    "1. Kaufe Semmeln",
    "2. Koche Kaffee",
    "3. Frühstücke",
]


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie eine Funktion `make_enumeration(items: list[str]) -> str`, die
# eine Aufzählung in der folgenden Form erzeugt:
#
# ```python
# make_enumeration(["Kaufe Semmeln", "Koche Kaffee", "Frühstücke"])
# '1. Kaufe Semmeln\n2. Koche Kaffee\n3. Frühstücke'
# ```

# %%
def make_enumeration(items: list[str]) -> str:
    return "\n".join(enumerate_items(items))


# %% lang="de" tags=["keep"]
assert (
    make_enumeration(["Kaufe Semmeln", "Koche Kaffee", "Frühstücke"])
    == "1. Kaufe Semmeln\n2. Koche Kaffee\n3. Frühstücke"
)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie eine Funktion `print_enumeration(items: list[str]) -> None`, die
# eine Aufzählung in der folgenden Form auf dem Bildschirm ausdruckt:
#
# ```python
# print_enumeration(["Kaufe Semmeln", "Koche Kaffee", "Frühstücke"])
# 1. Kaufe Semmeln
# 2. Koche Kaffee
# 3. Frühstücke
# ```


# %%
def print_enumeration(items: list[str]) -> None:
    print(make_enumeration(items))


# %% lang="de" tags=["keep"]
print_enumeration(["Kaufe Semmeln", "Koche Kaffee", "Frühstücke"])
