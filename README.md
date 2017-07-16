# pion
A Python 3 library for the Ion format


# Contributing

Useful links:

* [Ion Specification](https://amzn.github.io/ion-docs/spec.html)
* [ANTLR JavaDocs](http://www.antlr.org/api/Java/index.html?overview-summary.html)

* Change to the `pion` directory: `cd pion`
* Create a virtual environment: `virtualenv --python=python3 venv`
* Active the virtual environment: `source venv/bin/activate`

The core parser is created using [ANTLR](https://github.com/antlr/antlr4) from
the [Ion grammar](http://amzn.github.io/ion-docs/grammar/IonText.g4.txt). To
create the parser files, go to the `antlr` directory and download the ANTLR jar
and then run the following command:

    java -jar antlr-4.7-complete.jar -Dlanguage=Python3 IonText.g4
