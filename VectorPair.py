class VectorPair: 
    """
        Class defining a VectorPair object with helper methods.
        """
     def __init__(self, v1, v2, n): 
         """
         CConstructor takes in two vectors and the vector length
         """
         self.v1 = v1
         self.v2 = v2
         self.n = n

     def _resolve_sp(self, v1, v2): 
         """
         Given two vectors of equal length, the scalar product is pairwise 
         multiplication of values and the sum of all pairwise products. 
         """
         sp = 0

         # Iterate over elements in the array and compute 
         # the scalar product
         for i in range(self.n):
                 sp += v1[i] * v2[i]

         return sp

     def resolve_msp(self): 
         """
         Given two vectors of equal length, the minimum scalar product is
         the smallest number that exists given all permutations of
         multiplying numbers between the two vectors.
         """

         # Sort v1 low->high and v2 high->low
         # This ensures the smallest values of one list are 
         # paired with the largest values of the other 
         v1sort = sorted(self.v1, reverse=False)
         v2sort = sorted(self.v2, reverse=True)
         # Invoke the internal method for resolution
         return self._resolve_sp(v1sort, v2sort)
