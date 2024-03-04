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
#  <b>Mehr zu For-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 18 Mehr zu For-Schleifen.py -->
# <!-- python_courses/slides/module_150_collections/topic_154_destructuring_for.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Zuweisung an mehrere Variablen
#
# Wir haben schon gesehen, dass man an mehrere Variablen gleichzeitig zuweisen kann:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Das ist auch in `for`-Schleifen möglich:

# %% tags=["keep"]
values = [(1, "one"), (2, "two"), (3, "three")]

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Anzahl und Gesamtpreis
#
# In der folgenden Liste haben wir Name, Stückzahl und Preis pro Stück für eine Liste
# von Einkäufen gespeichert. Schreiben Sie eine Funktion
# `anzahl_und_gesamtpreis(artikel: list[tuple[int, float]]) -> tuple[int, float]`,
# die die Gesamtzahl der gekauften Artikel und den Gesamtpreis berechnet:
#
# ```python
# >>> anzahl_und_gesamtpreis([(3, 2.0), (5, 1.0)])
# (8, 11.0)
# ```

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% lang="de" tags=["keep"]
artikel = [(3, 2.0), (5, 1.0)]

# %% lang="de"
