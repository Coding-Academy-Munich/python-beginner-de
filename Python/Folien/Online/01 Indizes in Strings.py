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
#  <b>Indizes in Strings</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Indizes in Strings.py -->
# <!-- python_courses/slides/module_120_data_types/topic_175_a3_string_indexing.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Länge von Strings
#
# Mit der Funktion `len()` kann die Länge eines Strings bestimmt werden.

# %%
len("abc")

# %% tags=["keep"]
letters = "abcdefghijklmnopqrstuvwxyz"

# %%
len(letters)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Indizes in Strings
#
# - In Python ist es möglich, auf einzelne Buchstaben in Strings zuzugreifen.
# - Das Ergebnis ist wieder ein String (mit einem Buchstaben)
# - Die Syntax ist `string[index]`
# - Indizes beginnen ab 0!

# %%
letters

# %%
letters[0]

# %%
letters[3]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Gültige Indizes für einen String `text` sind zwischen 0 und `len(text) - 1`
# - Verwendung eines Index-Wertes `>= len(text)` führt zu einem Fehler
# - Mit negativen Indizes kann man vom rechten Ende des Strings indizieren

# %% tags=["keep"]
letters = "abcdefghijklmnopqrstuvwxyz"

# %%
letters[25]

# %%
# letters[26]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
letters[-1]

# %%
letters[-26]

# %%
# letters[-27]


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Slicing für Strings
#
# Mit dem Indexing-Operator `[]` kann auch ein längerer Teilstring eines Strings
# Extrahiert werden:


# %% tags=["keep"]
letters = "abcdefghijklmnopqrstuvwxyz"

# %%
letters[0:3]

# %%
letters[0:100]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
letters[:6]

# %%
letters[6:]

# %%
letters[:]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
letters[0:6:2]

# %%
letters[26:0:-1]

# %%
letters[26:-1:-1]

# %%
letters[26::-1]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: String Indexing
#
# Schreiben Sie eine Funktion `truncate(text: str, max_len: int)`, die den String
# `text` auf `max_len` Zeichen kürzt, falls er länger ist und ihn andernfalls
# unverändert lässt.
#
# Wie verhält sich Ihre Implementierung, wenn `max_len < 0` ist?


# %%
def truncate(text: str, max_len: int):
    return text[:max_len]


# %% tags=["keep"]
assert truncate("abc", 3) == "abc"

# %% tags=["keep"]
assert truncate("abcdefgh", 4) == "abcd"

# %% tags=["keep"]
assert truncate("abc", 0) == ""

# %% tags=["keep"]
truncate("abc", -1)
