class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n+1):
            temp = ""
            if not i%3: temp+= "Fizz"
            if not i%5: temp+= "Buzz"
            out.append(temp or str(i))
        return out
