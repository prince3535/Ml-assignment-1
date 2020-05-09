{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment 1 in MLD"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q.1 write a program which will find all such numbers which are divide by 7 but are not multiple of 5, between 2000 and 3000 (both included) . the numbers obtained should be printed in a comma seperated sequences of single line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2002\n",
      "2009\n",
      "2016\n",
      "2023\n",
      "2037\n",
      "2044\n",
      "2051\n",
      "2058\n",
      "2072\n",
      "2079\n",
      "2086\n",
      "2093\n",
      "2107\n",
      "2114\n",
      "2121\n",
      "2128\n",
      "2142\n",
      "2149\n",
      "2156\n",
      "2163\n",
      "2177\n",
      "2184\n",
      "2191\n",
      "2198\n",
      "2212\n",
      "2219\n",
      "2226\n",
      "2233\n",
      "2247\n",
      "2254\n",
      "2261\n",
      "2268\n",
      "2282\n",
      "2289\n",
      "2296\n",
      "2303\n",
      "2317\n",
      "2324\n",
      "2331\n",
      "2338\n",
      "2352\n",
      "2359\n",
      "2366\n",
      "2373\n",
      "2387\n",
      "2394\n",
      "2401\n",
      "2408\n",
      "2422\n",
      "2429\n",
      "2436\n",
      "2443\n",
      "2457\n",
      "2464\n",
      "2471\n",
      "2478\n",
      "2492\n",
      "2499\n",
      "2506\n",
      "2513\n",
      "2527\n",
      "2534\n",
      "2541\n",
      "2548\n",
      "2562\n",
      "2569\n",
      "2576\n",
      "2583\n",
      "2597\n",
      "2604\n",
      "2611\n",
      "2618\n",
      "2632\n",
      "2639\n",
      "2646\n",
      "2653\n",
      "2667\n",
      "2674\n",
      "2681\n",
      "2688\n",
      "2702\n",
      "2709\n",
      "2716\n",
      "2723\n",
      "2737\n",
      "2744\n",
      "2751\n",
      "2758\n",
      "2772\n",
      "2779\n",
      "2786\n",
      "2793\n",
      "2807\n",
      "2814\n",
      "2821\n",
      "2828\n",
      "2842\n",
      "2849\n",
      "2856\n",
      "2863\n",
      "2877\n",
      "2884\n",
      "2891\n",
      "2898\n",
      "2912\n",
      "2919\n",
      "2926\n",
      "2933\n",
      "2947\n",
      "2954\n",
      "2961\n",
      "2968\n",
      "2982\n",
      "2989\n",
      "2996\n"
     ]
    }
   ],
   "source": [
    "for i in range(2000,3000):\n",
    "    if (i%7==0 and i%5!=0):\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q.2 write a python program to accept the user's first and last name and then getting them printted in the reverse order with a space between first name and last name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "srivastava , Prince\n"
     ]
    }
   ],
   "source": [
    "# We can do this by two method, first is without user input and second is with user input.\n",
    "# A.\n",
    "fname=\"Prince\"\n",
    "lname=\"srivastava\"\n",
    "name=fname+lname\n",
    "print(name[6:],\",\",name[:6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first nameprince\n",
      "enter second namesrivastava\n",
      "final required output is: srivastava , prince\n"
     ]
    }
   ],
   "source": [
    "# B part of the above program \n",
    "fname=input(\"enter first name\")\n",
    "lname=input(\"enter second name\")\n",
    "name=fname+lname\n",
    "a=len(fname)\n",
    "print(\"final required output is:\",name[a:],\",\",name[:a])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q3 write a python program to find volume of the sphare with diemeter 12cm.\n",
    "formula v=(4/3)*(22/7)*r**3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "volume of sphare is: 905.142857142857\n"
     ]
    }
   ],
   "source": [
    "d=12        #d shows the diemeter\n",
    "r=d/2       #r shows the radious\n",
    "v=(4/3)*(22/7)*r**3  # v shows volume of sphare\n",
    "print(\"volume of sphare is:\",v)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
