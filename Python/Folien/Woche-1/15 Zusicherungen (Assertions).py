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
#  <b>Zusicherungen (Assertions)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 Zusicherungen (Assertions).py -->
# <!-- python_courses/slides/module_120_data_types/topic_150_b1_assertions.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Zusicherungen
#
# Zusicherungen (Assertions) sind eine gute Möglichkeit sicherzustellen, dass
# eine Eigenschaft erfüllt ist. Wenn die getestete Eigenschaft erfüllt ist,
# macht die Assertion nichts:

# %%
assert 1 == 1

# %%
assert 1 != 2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wenn die getestete Eigenschaft nicht erfüllt ist, wird ein Fehler ausgelöst:

# %%
# assert 1 == 2


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Mini-Workshop
#
# Gegeben seien die folgenden Anweisungen:

# %% tags=["keep"]
my_int = 1
my_float = 1.0

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie für jede der folgenden Eigenschaften eine Assertion, die
# entweder die Eigenschaft oder ihre Negation zusichert und keinen Fehler
# auslöst:
#
# - `my_int == 1`
# - `my_float == my_int`
# - `my_float == "1.0"`

# %%
assert my_int == 1
assert my_float == my_int
assert my_float != "1.0"
