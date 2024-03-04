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
#  <b>String Methoden (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 String Methoden (Teil 1).py -->
# <!-- python_courses/slides/module_120_data_types/topic_180_a3_string_methods_part1.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # String Methoden (Teil 1)
#
# Methoden sind ähnlich zu Funktionen, werden aber "auf einem Objekt" aufgerufen.
#
# Die Syntax ist `objekt.methode(...)`.
#
# In Text werden Methoden entweder als `Typ.methode()` oder `methode()` geschrieben.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Umwandeln eines Strings in Groß-/Kleinbuchstaben
#
# - `string.lower()` wandelt einen String in Kleinbuchstaben um
# - `string.upper()` wandelt einen String in Großbuchstaben um

# %% lang="de"
text = "Das ist ein Text"
print(text.lower())
print(text)

# %% lang="de"
"Das ist ein Text".upper()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die `lower()` und `upper()` Methoden wandeln Strings so um, dass sie ausgedruckt
# werden können. Für schreibungsunabhängige Vergleiche ist die `casefold()` Methode
# die korrekte Wahl.

# %%
s1 = "daß er sehe"
s1.upper()

# %%
s1.lower()

# %%
s1.casefold()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Shout
#
# Schreiben Sie eine Funktion `shout(text)`, die `text` in Großbuchstaben,
# gefolgt von drei Ausrufezeichen auf dem Bildschirm ausgibt.


# %%
def shout(text: str):
    print(f"{text.upper()}!!!")


# %% [markdown] lang="de"
# Testen Sie die Funktion mit Argument `"Hallo"`

# %% lang="de"
shout("Hallo")
