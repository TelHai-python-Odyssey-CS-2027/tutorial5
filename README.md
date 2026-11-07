# Tutorial 5 — Dictionaries, histograms, SymPy

Practice for lecture 5: dictionaries, building a histogram, and a first look at SymPy.

**Colab from GitHub:** a normal click stays in the same tab (GitHub removes “open in a new tab”). Use **Ctrl+click** (Windows/Linux) or **⌘+click** (Mac), or middle-click, to open Colab in a new tab.

- <a href="https://colab.research.google.com/github/TelHai-python-Odyssey-CS-2027/tutorial5/blob/main/dictionary_basic.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Dictionary"/></a> `dictionary_basic.ipynb`
- <a href="https://colab.research.google.com/github/TelHai-python-Odyssey-CS-2027/tutorial5/blob/main/histogram.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Histogram"/></a> `histogram.ipynb`
- <a href="https://colab.research.google.com/github/TelHai-python-Odyssey-CS-2027/tutorial5/blob/main/sympy_tutorial.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="SymPy"/></a> `sympy_tutorial.ipynb`

## Files

| File | Role |
| --- | --- |
| `dictionary_basic.ipynb` | Dictionary warm-up (practice only) |
| `histogram.ipynb` | Implement `build_histogram` with self-check |
| `histogram_utils.py` | Graded module — put your finished function here |
| `examples.py` | Sample data for the histogram notebook |
| `self_checks.py` | Self-check helpers called from the histogram notebook |
| `sympy_tutorial.ipynb` | SymPy intro (practice only) |

## How to work

1. Open the notebooks in Colab (buttons above) or locally.
2. In the histogram notebook, implement `build_histogram`, then run the **self-check** cell (loads `self_checks.py`).
3. Copy the finished function into `histogram_utils.py` and **Commit changes** to see the practice autograding score (5 points).

Also add the `matplotlib.pyplot` import (as `plt`) at the top of `histogram_utils.py` so `plot_histogram` can run — that import is not graded.

## Grading — 5 points (practice)

| Check | Points |
| --- | ---: |
| `build_histogram` — basic frequencies | 1 |
| `build_histogram` — empty list | 1 |
| `build_histogram` — all identical | 1 |
| `build_histogram` — strings | 1 |
| `build_histogram` — mixed ints | 1 |

## Optional: keep your changes in Google Drive

In Colab: **File → Save a copy in Drive**.
