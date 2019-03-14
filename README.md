# MUSHPy

This repository contains tests of the [AlignmentRepaPy repository](https://github.com/caiks/AlignmentRepaPy) using data from the [UCI Machine Learning Repository Mushroom Data Set](https://archive.ics.uci.edu/ml/datasets/mushroom). The AlignmentRepaPy repository is a fast Python implementation of some of the *practicable inducers* described in the paper *The Theory and Practice of Induction by Alignment* at https://greenlake.co.uk/. 

## Documentation

There is an analysis of this dataset [here](https://greenlake.co.uk/pages/dataset_MUSH), with sections (a) [predicting edibility without modelling](https://greenlake.co.uk/pages/dataset_MUSH#Predicting_edibility_without_modelling), (b) [predicting odor without modelling](https://greenlake.co.uk/pages/dataset_MUSH#Predicting_odor_without_modelling), (c) [manual modelling of edibility](https://greenlake.co.uk/pages/dataset_MUSH#Manual_modelling_of_edibility) and (d) [induced modelling of edibility](https://greenlake.co.uk/pages/dataset_MUSH#Induced_modelling_of_edibility). 

## Installation

The `MUSH` executables require the `AlignmentRepa` module which is in the [AlignmentRepaPy repository](https://github.com/caiks/AlignmentRepaPy). See the AlignmentRepaPy repository for installation instructions of the Python compiler and libraries.

Then download the zip files or use git to get the `MUSHPy` repository and the underlying `AlignmentPy` and `AlignmentRepaPy` repositories -
```sh
cd
git clone https://github.com/caiks/AlignmentPy.git
git clone https://github.com/caiks/AlignmentRepaPy.git
git clone https://github.com/caiks/MUSHPy.git
```

## Usage

To experiment with the dataset in the interpreter,
```sh
cd MUSHPy
export PYTHONPATH=../AlignmentPy:../AlignmentRepaPy
python3
```
```py
from MUSHDev import *

(uu,aa) = mushIO()
vv = uvars(uu)
vvl = sset([VarStr("edible")])
vvk = vv - vvl

hr = aahr(uu,aa)

(wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed) = ((9*9*10), 8, (9*9*10), 10, (10*3), 3, (9*9*10), 1, 3, 3, 5)

(uu1,df1) = decomperIO(uu,vvk,hr,wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed)

open("df.json","w").write(decompFudsPersistentsEncode(decompFudsPersistent(df1)))

summation(mult,seed,uu1,df1,hr)
(61302.44944051167, 26729.333546815153)
```


