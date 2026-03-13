# Implement `wc` in python

You should already be familiar with the `wc` command line tool.

Your task is to implement your own version of `wc`.

It must act the same as `wc` would, if run from the directory containing this README.md file, for the following command lines:

* `wc sample-files/*`
* `wc -l sample-files/3.txt`
* `wc -w sample-files/3.txt`
* `wc -c sample-files/3.txt`
* `wc -l sample-files/*`

Matching any additional behaviours or flags are optional stretch goals.

We recommend you start off supporting no flags for one file, then add support for multiple files, then add support for the flags.

*======Command for testing the script========

* All sample files
python wc.py sample-files/*

* Just lines
python wc.py -l sample-files/3.txt

* Just words
python wc.py -w sample-files/3.txt

* Just characters
python wc.py -c sample-files/3.txt

* Lines with multiple files (to see totals)
python wc.py -l sample-files/*
