import math
from dists import dists, straight_line_dists_from_bucharest

excluded_list = set()

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
  """
  Retorna uma lista com o caminho de start até 
  goal segundo o algoritmo A*
  """
  global excluded_list

  excluded_list.add(start)

  if start == goal: return [start]

  selected_city = select_city(dists[start])
  
  return [start] + a_star(selected_city)

def select_city(neighboring_cities):
  global excluded_list
  selected = None
  total_dist = None
  city_dist = None

  for city in neighboring_cities:
    city_dist = city_total_dist(city)

    if city[0] not in excluded_list and (selected is None or city_dist < total_dist):
      selected = city[0]
      total_dist = city_dist

    excluded_list.add(city[0])

  return selected

def city_total_dist(city):
  return straight_line_dists_from_bucharest[city[0]] + city[1]
