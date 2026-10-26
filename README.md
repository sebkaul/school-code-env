# school-code-env

Python scripts for chemical engineering courses: lab data analysis, exercise solutions and plots. Each folder is named after a course code.

## Setup and running

Uses [uv](https://docs.astral.sh/uv/) and Python 3.14. `uv sync` installs numpy, scipy, pandas, matplotlib and PyQt6 (the matplotlib GUI backend).

```sh
uv sync
uv run imak2004/titrerkurve.py
```

Scripts that import sibling modules (e.g. `kp3010/Øving 3 Python/`), and everything in `imat3012/` (own `pyproject.toml`, adds sympy), must be run from their own folder:

```sh
cd imat3012 && uv run ex2opg10b.py
```

Lab scripts have an input block at the top (`=== EDIT THIS FOR EACH LAB ===`, `INPUT` or `FYLL INN`) for the measured data. New plots (`*.png`) are git-ignored.

## Contents

| Folder | What's in it |
| --- | --- |
| `imak2003/` | Lineweaver–Burk plots, standard curves |
| `imak2004/` | GC and HPLC standard curves, weak acid titration curve |
| `imak2005/` | Mass balances with `scipy.optimize`, Lineweaver–Burk plot |
| `imak2008/` | Bradford protein standard curve, caffeine HPLC with external and internal calibration |
| `imat3012/` | Math with sympy and scipy: derivatives, integrals (incl. Monte Carlo), matrices |
| `kp3010/` | Absorption: McCabe–Thiele, stage-by-stage column model |
| `matv1007/` | E. coli growth curve, with and without exponential regression |
| `tkp4110/` | Reaction engineering exercises (reactor sizing, kinetics, Langmuir fit, non-isothermal CSTR) and the RE1 (biodiesel) and RE3 (t-butyl chloride CSTR) labs |
| `python-mal.py` | Linear regression / Lineweaver–Burk template: edit `x` and `y` and run |
