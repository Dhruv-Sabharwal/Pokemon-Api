from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.template import loader
from .models import Pokemon
import json


def index(request):
    return HttpResponse("Welcome to the Pokedex!")

def search(request):
    template=loader.get_template('webapi/search.html')
    return_list = []
    name_query=request.GET.get('name')
    attack_query=request.GET.get('attack')
    defense_query=request.GET.get('defense')
    pokedex_num_query=request.GET.get('pokedex_num')
    attack_defense_query=request.GET.get('attack_defense')
    legendary_query=request.GET.get('legendary')
    type_query=request.GET.get('type')
    total_query=request.GET.get('total')
    
    if name_query:
    	print("hello name")
    	poke = Pokemon.objects.all().filter(Q(name__icontains=name_query)).distinct()
    
    else:
    	poke = Pokemon.objects.all()

    if attack_defense_query:
    	print("hello a&d")
    	poke = poke.filter(Q(attack__gt=attack_defense_query)&Q(defense__gt=attack_defense_query)).distinct()

    if attack_query:
    	print("hello att")
    	poke = poke.filter(Q(attack__gt=attack_query)).distinct()
    	

    if defense_query:
    	print("hello def")
    	poke = poke.filter(Q(defense__gt=defense_query)).distinct()

    if pokedex_num_query:
    	print("hello pokedex")
    	poke = Pokemon.objects.all().filter(Q(pokedex_num__icontains=pokedex_num_query)).distinct()

    if legendary_query:
    	print("hello legen")
    	poke = Pokemon.objects.all().filter(Q(legendary__icontains=legendary_query)).distinct()

    if total_query:
    	print("hello total")
    	poke = poke.filter(Q(total__gt=total_query)).distinct()

    if type_query:
    	print("hello type")
    	poke = Pokemon.objects.all().filter(Q(type_1__icontains=type_query)|Q(type_2__icontains=type_query)).distinct()
    	

    data = {}
    for each in poke:
        try:
            data[each.name].append({'pokedex_num' : each.pokedex_num,
            						'name' : each.name,
            						'type_1' : each.type_1,
            						'type_2' : each.type_2,
            						'total' : each.total,
                                    'hp' : each.hp,
                                    'attack' : each.attack,
                                    'defense' : each.defense,
                                    'sp_attack' : each.sp_attack,
                                    'sp_defense' : each.sp_defense,
                                    'speed': each.speed,
                                    'generation:' : each.generation,
                                    'legendary': each.legendary})
        except KeyError:
            data[each.name] = [{'pokedex_num' : each.pokedex_num,
            					'name' : each.name,
            					'type_1' : each.type_1,
            					'type_2' : each.type_2,
            					'total' : each.total,
                                'hp' : each.hp,
                                'attack' : each.attack,
                                'defense' : each.defense,
                                'sp_attack' : each.sp_attack,
                                'sp_defense' : each.sp_defense,
                                'speed': each.speed,
                                'generation:' : each.generation,
                                'legendary': each.legendary}]
    context = {
        'data' : json.dumps(data),
    }
    return HttpResponse(template.render(context, request))


