#python 3.5.2

def find_min(A):
   ans = 0
   for i in range(1, len(A)):
       if A[i] < ans:
          ans = A[i]
   return ans

def solution(N):
   array = []
   for i in range(N, N + N):
       array.append(i)
   return array

A = solution(4)
print(A)

minValue = find_min(A)
print(minValue)
