{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os,sys\n",
    "from os.path import dirname, join, abspath\n",
    "\n",
    "sys.path.insert(0,abspath(join(dirname(__file__),'..')))\n",
    "\n",
    "from payment import payment_details\n",
    "def course():\n",
    "    print(\"this is my coursee detailss\")\n",
    "    \n",
    "payment_details.payment()"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
