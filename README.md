# school-code-env

Simple Python scripts for chemical engineering courses: lab data analysis, exercise solutions and plots. Each folder is named after a course code.

## Setup

The project uses [uv](https://docs.astral.sh/uv/) and Python 3.14 (see `.python-version`).

```sh
uv sync
```

This installs numpy, scipy, pandas, matplotlib and PyQt6 (used as the matplotlib GUI backend).

## Running a script

```sh
uv run imak2004/titrerkurve.py
```

Some scripts import sibling modules. Run those from their own folder:

```sh
cd "kp3010/Øving 3 Python"
uv run main.py
```

`imat3012/` has its own `pyproject.toml` (it also needs sympy), so run its scripts from inside that folder:

```sh
cd imat3012
uv run ex2opg10b.py
```

## Contents

| Folder | What's in it |
| --- | --- |
| `imak2003/` | Lab analysis: Lineweaver–Burk plots (`lab1.py`) and standard curves (`lab3.py`) |
| `imak2004/` | GC and HPLC standard curves, weak acid titration curve |
| `imak2005/` | Mass balances solved with `scipy.optimize` (caffeine extraction, sulphur filtration), Lineweaver–Burk plot |
| `imat3012/` | Math exercises with sympy: derivatives, single and double integrals, matrices |
| `kp3010/` | Absorption: McCabe–Thiele for a linear-equilibrium absorber, stage-by-stage absorption column model |
| `matv1007/` | E. coli growth curve with and without exponential regression |
| `tkp4110/` | Reaction engineering: reactor sizing from Levenspiel data, batch kinetics, Michaelis–Menten, and the RE1 biodiesel lab (GC analysis, conversion and selectivity) |
| `python-mal.py` | Template for a linear regression / Lineweaver–Burk plot. Edit the `x` and `y` arrays and run it |

Most lab scripts have a marked `=== EDIT THIS FOR EACH LAB ===` block at the top where you enter the measured data.
