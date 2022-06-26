class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        city_map = {}
        for cityA, cityB in paths:
            city_map[cityA] = cityB
        
        for city in city_map.values():
            if city not in city_map.keys():
                return city
        
        # City with no outgoing nodes is answer
        # O(n)
#         outgoing_count = {}
#         for cityA, cityB in paths:
#             outgoing_count[cityA] = outgoing_count.get(cityA, 0) + 1
#             outgoing_count[cityB] = outgoing_count.get(cityB, 0)
            
#         for city in outgoing_count:
#             if outgoing_count[city] == 0:
#                 return city