# MUSHPy

This repository contains tests of the [AlignmentRepaPy repository](https://github.com/caiks/AlignmentRepaPy) using data from the [UCI Machine Learning Repository Mushroom Data Set](https://archive.ics.uci.edu/ml/datasets/mushroom). The AlignmentRepaPy repository is a fast Python implementation of some of the *practicable inducers* described in the paper *The Theory and Practice of Induction by Alignment* at https://greenlake.co.uk/. 

## Documentation

There is an analysis of this dataset [here](https://greenlake.co.uk/pages/dataset_MUSH), with sections (a) [predicting edibility without modelling](https://greenlake.co.uk/pages/dataset_MUSH#Predicting_edibility_without_modelling), (b) [predicting odor without modelling](https://greenlake.co.uk/pages/dataset_MUSH#Predicting_odor_without_modelling), (c) [manual modelling of edibility](https://greenlake.co.uk/pages/dataset_MUSH#Manual_modelling_of_edibility) and (d) [induced modelling of edibility](https://greenlake.co.uk/pages/dataset_MUSH#Induced_modelling_of_edibility). 

## Installation

The `MUSH` executables require the `AlignmentRepa` module which is in the [AlignmentRepa repository](https://github.com/caiks/AlignmentRepa). See the AlignmentRepa repository for installation instructions of the Haskell compiler and libraries.

Then download the zip files or use git to get the MUSH repository and the underlying Alignment and AlignmentRepa repositories -
```
cd
git clone https://github.com/caiks/Alignment.git
git clone https://github.com/caiks/AlignmentRepa.git
git clone https://github.com/caiks/MUSH.git
```

## Usage

The *practicable model induction* is described [here](https://greenlake.co.uk/pages/dataset_MUSH_model16).

`MUSH_engine16` runs on a Ubuntu 16.04 Pentium CPU G2030 @ 3.00GHz using 1784 MB total memory and takes 1166 seconds,

```
cd ../Alignment
rm *.o *.hi

cd ../AlignmentRepa
rm *.o *.hi

gcc -fPIC -c AlignmentForeign.c -o AlignmentForeign.o -O3

cd ../MUSH
rm *.o *.hi

ghc -i../Alignment -i../AlignmentRepa ../AlignmentRepa/AlignmentForeign.o MUSH_engine16.hs -o MUSH_engine16.exe -rtsopts -O2

./MUSH_engine16.exe +RTS -s >MUSH_engine16.log 2>&1 &

tail -f MUSH_engine16.log

```

To experiment with the dataset in the interpreter,
```
cd ../Alignment
rm *.o *.hi

cd ../AlignmentRepa
rm *.o *.hi

gcc -fPIC -c AlignmentForeign.c -o AlignmentForeign.o -O3

cd ../MUSH

ghci -i../Alignment -i../AlignmentRepa ../AlignmentRepa/AlignmentForeign.o
```

```hs
:set -fobject-code
:l MUSHDev
```
Then exit the interpreter,
```
rm MUSHDev.o

ghci -i../Alignment -i../AlignmentRepa ../AlignmentRepa/AlignmentForeign.o
```

```hs
:l MUSHDev

mush <- ByteStringChar8.readFile "../MUSH/agaricus-lepiota.data"

let aa = llaa $ map (\ll -> (llss ll,1)) $ map (\ss -> (map (\(u,(v,uu)) -> (VarStr v,ValStr (fromJust (lookup u uu)))) (zip ss names))) $ map (\l -> filter (/=',') l) $ lines $ ByteStringChar8.unpack $ mush
let uu = sys aa
let vv = uvars uu
let vvl = Set.singleton (VarStr "edible")
let vvk = vv `minus` vvl
let hh = aahr uu aa

let (wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed) = ((9*9*10), 8, (9*9*10), 10, (10*3), 3, (9*9*10), 1, 3, 3, 5)

Just (uu1,df1) <- decomperIO uu vvk hh wmax lmax xmax omax bmax mmax umax pmax fmax mult seed

ByteString.writeFile ("df1.json") $ decompFudsPersistentsEncode $ decompFudsPersistent df1

summation mult seed uu1 df1 hh
(54409.95661501111,24589.66463393197)

```


