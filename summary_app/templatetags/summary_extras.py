from django import template 
import numpy as np

register = template.Library()

@register.filter(name = 'max_lat')
def max_lat(value):
    arr = np.array(value)
    arr_fl = arr.flatten()
    return np.max(arr_fl[0::2])
	

@register.filter(name = 'min_long')
def min_long(value):
    arr = np.array(value)
    arr_fl = arr.flatten()
    return np.min(arr_fl[1::2])
	
@register.filter(name = 'min_lat')
def min_lat(value):
    arr = np.array(value)
    arr_fl = arr.flatten()
    return np.min(arr_fl[0::2])
	

@register.filter(name = 'max_long')
def max_long(value):
    arr = np.array(value)
    arr_fl = arr.flatten()
    return np.max(arr_fl[1::2])
    
