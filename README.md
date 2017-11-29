Two views on regression with PyMC3 and scikit-learn
===================================================
Presentation at PyData NYC 2017

Installation
------------
```
git clone https://github.com/ColCarroll/pydata_nyc2017.git
conda env create -f environment.yml
```

I have also included a `requirements.txt` if pip is more your thing.  `pip install -r requirements.txt`

Guaranteed to probably work with Python3.6.3.  You'll have even more fun if you 
`pip install --upgrade git+https://github.com/pymc-devs/pymc3`.  Maximum fun if 
you also `pip install -U theano==1.0.0` (NOTE: PyMC3 tests still do not pass on Theano 1.0.0, and 
I won't answer any of your questions if you are having this much fun).

To view
-------
```
source activate pydata_nyc20173.6
jupyter notebook
```

These can be viewed as a slideshow using the RISE plugin 
(see https://github.com/damianavila/RISE), which should get installed 
automatically.  You are on your own if you are using pip, though.  Look for the button on your Jupyter toolbar.
