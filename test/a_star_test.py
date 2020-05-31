from a_star import a_star, select_city
from dists import dists

def test_a_star():
  assert a_star('Lugoj') == ['Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Pitesti', 'Bucharest']

def test_select_city():
  assert select_city(dists['Arad']) == 'Sibiu'
  assert select_city(dists['Iasi']) == 'Vaslui'
  assert select_city(dists['Hirsova']) == 'Urzineci'
