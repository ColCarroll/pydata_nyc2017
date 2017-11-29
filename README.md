Two views on regression with PyMC3 and scikit-learn
===================================================

These can be run as a slideshow using the RISE plugin (see https://github.com/damianavila/RISE for installation instructions).

They can also be perused and run on their own:

```
git clone https://github.com/ColCarroll/pydata_nyc2017.git
conda env create -f environment.yml
```

I have also included a `requirements.txt` if pip is more your thing.  `pip install -r requirements.txt`

Guaranteed to probably work with Python3.6.3.  You'll have even more fun if you 
`pip install --upgrade git+https://github.com/pymc-devs/pymc3`.  Maximum fun if 
you also `pip install -U theano==1.0.0` (NOTE: PyMC3 tests still do not pass on Theano 1.0.0, and 
I won't answer any of your questions if you are having this much fun).
