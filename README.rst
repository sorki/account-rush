account-rush
============

Tool to generate a custom, valid Czech bank account numbers according to
user provided number pairs.

In Czech Republic, it's now possible to choose your own bank account number.
While we have better tools to manage ones finances (like digital currencies..)
it will still take a while until we can get rid of our classic bank accounts.
So why not making our lives easier by creating a number that's easy to memorize
and is composed of your favorite number sequences!

Czech bank account number has to comply with following regulations of CNB:

 - at least 8 characters
 - maximum 10 characters
 - has to pass modulo 11 check (weighted sum has to be divisible by 11)

Source: http://www.cnb.cz/cs/platebni_styk/pravni_predpisy/download/vyhl_62_2004_p1.pdf

Usage
-----

Clone this repository::

  git clone https://github.com/sorki/account-rush.git
  cd account-rush

Use the tool to generate possible account numbers using your favorite number sequences::

  ./gen.py 666 1337 42 777 13 555

Or check one or more numbers for validity::

  ./gen.py --check 777133742
  777133742 is valid
