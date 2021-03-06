import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import *
from util import *
from predicates import *
import random


@action
@given(player, string)
def check_scope_while(e, a):
  res = act("check_scope", e, location(e)) 
  return res

@action
@given(player, equals("look"))
def check_scope_while(e, a):
  return act("check_scope", e) 

@action
@given(player, equals("walk"))
def check_scope_while(e, a):
  return the(location(e),"exits").keys()

@action
@given(player, equals("drop"))
def check_scope_while(e, a):
  return act("check_inventory_scope", e) 

@action
@given(player, equals("drop"), anything)
def check_scope_while(e, a, b):
  inv = act("check_inventory_scope", e) 
  loc = location(e)
  res = act("check_scope", e, loc)
  return inv + res

@action
@given(player, equals("take"))
def check_scope_while(e, a):
  "(player, equals('take'))"
  return act("check_scope", e, location(e))

@action
@given(player)
def check_scope(a):
  inv = act("check_inventory_scope", a) 
  loc = location(a)
  res = act("check_scope", a, loc)
  return inv + res

@action
@given(a(player, container))
def check_inventory_scope(a):
  return contents_of(a)

@action
@given(entity, thing)
def check_scope(a, c):
  return [c]


@action
@given(entity, container)
def check_scope(a, b):
  if player(a) and player(b) and a != b: return []
  res = [b]
  for item in contents_of(b):
    f = act("check_scope", a, item)
    if f: 
      res += f
  return res





@action
@given(entity, a(hidden, thing))
def check_scope(a, c):
  return False
