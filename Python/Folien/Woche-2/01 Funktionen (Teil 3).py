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
#  <b>Funktionen (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Funktionen (Teil 3).py -->
# <!-- python_courses/slides/module_130_functions/topic_120_b1_functions_part3.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Funktionen ohne Parameter
#
# - Eine Funktion kann auch ohne formale Parameter definiert werden.
# - Sowohl bei der Definition, als auch beim Aufruf müssen die Klammern
#   trotzdem angegeben werden.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def null():
    return 0


# %% lang="de"
null()


# %% lang="de"
# Fehler: 'Aufruf' ohne Klammern
null

# %% lang="de"
# Fehler: 'Aufruf' ohne Klammern
# null + 1

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Funktionen mit Seiteneffekten
#
# Funktionen können
#
# - Werte berechnen: `round(3.3)`
# - Seiteneffekte haben: `print("Hans")`

# %%
round(3.3)

# %%
print("Hans")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Das gilt auch für benutzerdefinierte Funktionen:

# %%
def add1(x):
    return x + 1


# %%
add1(10)

# %%
def say_hi(name):
    print("Hi", name)


# %%
say_hi("John")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Der Rückgabewert `None`
#
# - Der Rückgabewert der Funktion `print()` ist der spezielle Wert `None`.
# - Dieser Wert wird vom Notebook nicht *als Ergebnis* angezeigt.

# %%
say_hi("Hans")

# %%
x = say_hi("Hans")
x is None

# %%
print(None)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# - Funktionen können Seiteneffekte haben
#     - Z.B. durch Aufruf von `print`
# - Diese werden ausgeführt, wenn ein Funktionsaufruf ausgewertet wird
# - Auch Funktionen mit Seiteneffekten geben einen Wert zurück
#     - Oft ist das der spezielle Wert `None`
#     - Wenn eine Funktion `None` zurückgibt brauchen wir keine explizite
#       `return`-Anweisung

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def say_hello():
    print("Hello, world!")
    print("Today is a great day!")


# %%
say_hello()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Piraten (Teil 2)
#
# In einer früheren Aufgabe haben wir die Aufteilung der Beute für Ihre
# Piratencrew folgendermaßen berechnet:
#
# - Die Beute wird gleichmäßig auf alle Piraten verteilt. Dabei werden nur
#   ganze Golddublonen ausgezahlt.
# - Den Rest der Golddublonen erhält der Kapitän.


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Jetzt droht Ihre Piraten-Crew aber zu meutern, weil die Berechnung der
# Beuteaufteilung zu lange dauert.
#
# Schreiben Sie eine Funktion `drucke_aufteilung_der_beute(dublonen, piraten)`,
# die die Aufteilung berechnet und in folgendem Format ausgibt:
#
# ```
# Piraten: 8
# Golddublonen: 17
# Jeder Pirat erhält: 2 Golddublone(n)
# Kapitän erhält extra: 1 Golddublone(n)
# ```

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def drucke_aufteilung_der_beute(dublonen, piraten):
    dublonen_pro_pirat = dublonen // piraten
    dublonen_kapitän = dublonen % piraten
    print("Piraten:", piraten)
    print("Golddublonen:", dublonen)
    print("Jeder Pirat erhält:", dublonen_pro_pirat, "Golddublone(n)")
    print("Kapitän erhält extra:", dublonen_kapitän, "Golddublone(n)")


# %% lang="de"
drucke_aufteilung_der_beute(17, 8)
