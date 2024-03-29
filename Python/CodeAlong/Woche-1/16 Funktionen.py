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
#  <b>Funktionen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 16 Funktionen.py -->
# <!-- python_courses/slides/module_130_functions/topic_110_b1_functions.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Funktionen
#
# Wir haben eine Firma zum Einzäunen dreieckiger Grundstücke gegründet.
#
# Für jedes von Straßen $A$, $B$ und $C$ begrenze Grundstück berechnen wir:

# %% lang="de" tags=["keep"]
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
länge_c = (länge_a**2 + länge_b**2) ** 0.5
länge_gesamt = länge_a + länge_b + länge_c
print(länge_gesamt)

# %% [markdown] lang="de"
# Können wir das etwas eleganter gestalten?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Satz von Pythagoras
#
# Wir berechnen die Länge von $C$ aus $A$ und $B$ immer nach dem Satz von
# Pythagoras: $C = \sqrt{A^2 + B^2}$.
#
# Das können wir in Python durch eine *Funktion* ausdrücken:

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Funktionsdefinition
# - Schlüsselwort `def`
# - Name der Funktion
# - Parameter der Funktion, in Klammern
# - **Doppelpunkt**
# - Rumpf der Funktion, *4 Leerzeichen eingerückt*
# - Im Rumpf können die Parameter wie Variablen verwendet werden
# - Schlüsselwort `return`
#     - Beendet die Funktion
#     - Bestimmt welcher Wert zurückgegeben wird

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Funktionsaufruf
#
# - Name der Funktion
# - Argumente des Aufrufs, in Klammern
# - Ein Argument für jeden Parameter

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Mini-Workshop
#
# Schreiben Sie eine Funktion `begrüßung(name)`, die eine Begrüßung in der Form
# "Hallo *name*!" zurückgibt, z.B.
# ```python
# >>> begrüßung("Max")
# 'Hallo Max!'
# >>>
# ```
#
# *Hinweis:* Sie können Strings mit dem `+`-Operator konkatenieren:
# ```python
# >>> name = "Max"
# >>> "Hallo, " + name
# 'Hallo, Max'
# ```

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Mini-Workshop: Funktionen die sich selbst aufrufen
#
# Schreiben Sie eine Funktion `fakultät(n)`, die die Fakultät einer Zahl `n`
# berechnet.
#
# *Hinweis:* Die Fakultät von 0 ist 1, die Fakultät von 1 ist 1, und die Fakultät
# von n ist n mal die Fakultät von n-1.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% lang="de" tags=["keep"]
assert fakultät(0) == 1
assert fakultät(1) == 1
assert fakultät(2) == 2
assert fakultät(5) == 120
