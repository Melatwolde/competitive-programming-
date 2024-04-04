class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order_dict = {}
        for index, element in enumerate(arr2):
            
            
            order_dict[element] = index
        
        def custom_sort_key(x):
            return (order_dict.get(x, float('inf')), x)
        
        arr1.sort(key=custom_sort_key)
        return arr1