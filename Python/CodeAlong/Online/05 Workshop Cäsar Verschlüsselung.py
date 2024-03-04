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
#  <b>Workshop: Cäsar Verschlüsselung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Workshop Cäsar Verschlüsselung.py -->
# <!-- python_courses/slides/projects/project_120_caesar_cipher.py -->

# %% [markdown] lang="de"
# ## Cäsar-Verschlüsselung
#
# Bei der Cäsar-Verschlüsselung werden die Buchstaben des zu verschlüsselnden
# Wortes im Alphabet um 3 Stellen verschoben, z.B. wird aus der Zeichenkette
# `ABC` die Zeichenkette `DEF`. Die letzten drei Buchstaben des Alphabets
# werden durch die ersten ersetzt, d.h. aus `XYZA` wird `ABCD`.
#
# Typischerweise wurden bei historischen Verschlüsselungsverfahren alle
# Buchstaben in Großbuchstaben umgewandelt. Leer- und Sonderzeichen werden
# ignoriert. So wird aus "Ich kam, sah und siegte." der verschlüsselte Text
#
# ```
# LFKNDPVDKXQGVLHJWH
# ```

# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `encode_char(c: str)`, die einen String `c`,
# der nur aus einem einzigen Zeichen besteht, folgendermaßen verschlüsselt:
#
# - ist `c` einer der Buchstaben `a` bis `z` oder `A` bis `Z` so wird er, falls
#   nötig, in einen Großbuchstaben umgewandelt und mit der Cäsar-Verschlüsselung
#   verschlüsselt;
# - ist `c` eine Ziffer, so wird sie unverändert zurückgegeben;
# - andernfalls wird der leere String `""` zurückgegeben.
#
# *Hinweis:* Die folgenden beiden Strings sind dabei hilfreich:

# %%

# %%

# %% [markdown] lang="de"
# Testen Sie Ihre Implementierung mit einigen Werten

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `encode_caesar(text: str)`, die einen String
# `text` mittels der Cäsar-Verschlüsselung verschlüsselt.

# %%

# %% [markdown] lang="de"
# Überprüfen Sie Ihr Programm mit den folgenden Beispielen:

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# Schreiben Sie jetzt Funktionen `decode_char(c: str)`
# und `decode_caesar(text: str)`, die einen mit der Cäsar-Verschlüsselung
# verschlüsselten Text entschlüsseln. Um robust zu sein, sollen diese
# Funktionen Zeichen, die keine Buchstaben oder Ziffern sind, unverändert zurückgeben.

# %%

# %%

# %%

# %% [markdown] lang="de"
# Testen Sie `decode_caesar()` mit `pangram` und `verlaine`.

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
# Entschlüsseln Sie den folgenden Text:
# ```
# SDFN PB ERA ZLWK ILYH GRCHQ OLTXRU MXJV
# (SDQJUDP IURP QDVD'V VSDFH VKXWWOH SURJUDP)
# ```

# %%

# %% [markdown] pycharm={"is_executing": false, "name": "#%% md\n"} lang="de"
# Die Funktionen `encode_char()` und `decode_char()` enthalten viel duplizierten
# Code. Können Sie eine Funktion `rot_n_char(...)` schreiben, die die
# Funktionalität beider Funktionen verallgemeinert?

# %%

# %% [markdown] lang="de"
#
# Wie würden Sie `encode_caesar_2()` und `decode_caesar_2()` unter
# Zuhilfenahme dieser Funktion implementieren?

# %%

# %%

# %% [markdown] lang="de"
# Testen Sie die neue Funktion mittels `secret_text` und `verlaine`.
# Sind alte und neue Implementierung kompatibel?

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
# Möglicherweise zeigt die Decodierung mit dem ursprünglichen Cäsar-Code, dass Ihre neue
# Implementierung einen Fehler hat, der bei der Verallgemeinerung häufig passiert:
# Es kann sein, dass der generalisierte Code Zahlen und Buchstaben vermischt.
#
# Gratulation, falls Sie diesen Fehler vermieden haben!
# Wie können wir den Fehler beseitigen, falls er bei Ihnen auftritt?

# %%

# %%

# %% [markdown] lang="de"
# Testen Sie die neue Implementierung indem Sie `secret_text` decodieren.

# %%

# %% [markdown] lang="de"
# Testen Sie die neue Implementierung mit `verlaine`.

# %%

# %%

# %%

# %%
