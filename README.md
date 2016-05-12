# Prime-numbers
Find prime numbers (Mersenne)
The way that u find a prime number of the wat 2^n-1 its:
1. you need a sequence: it start with 4
  the next number its the previous (number^2)-2, we can say n = ((n-1)^2)-2
2. you need the n-1th position in the sequence ie
  if u have 2^3-1 = 7; n =3, so u see the number in the sequence in the position n-1 (2)
  the sequence will be 4,14 <- our number
  then u see if the number of the sequence its a multiple of our number
  14 its multiple of 7, so we can say 7 its prime
3. The number in the sequence will be so big with a bigger n, so, if the number in the sequence its
    longer than our number, we can use the remainder of that. ie 14>7 so we only need the remainder 14%7
    and thats our new number on the sequence.
