# Exercise from https://app.codility.com/programmers/trainings/9/sparse_binary_decomposition/
def solution(N):
  # Sparce decomposition always exists for the range of inputs for this exercise, so never need to return -1
  # Bitwise and with (101010101010101010101010101010)_2 since inputs range up to 1,000,000,000 which is 30 digits when represented in binary
  # So by doing a bitwise and with a 30 digit binary number with a 1 in each odd power of 2's place and a zero in all other places, we
  # always get a number P which has a sparce binary representation and for which N-P also has a sparce binary representation.
  # If we were to take inputs with up to M digits in binary, we would simply do a bitwise and with a number of the form
  # sum from i=0 to floor(M/2) of 2**(2*i). In that case, we have 1's in the even power of 2's places, but it would still work the same
  return N & 715827882
