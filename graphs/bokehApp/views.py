from itertools import count
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from .models import Hospitalizations
from bokeh.resources import CDN

"""
    plot = figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size = 20, color = "blue")

    script, div = components(plot)
"""
#=======================================================================================

def starter(request):
    shoes = 0
    belts = 0
    shirts = 0
    counts = []

    items = ["Shoes", "Belts", "Shirts"]
    patients = (Hospitalizations.objects.values_list('HospiPati', flat=True))
    weeks = (Hospitalizations.objects.values_list('HospiWeeks', flat=True))



    plot = figure( plot_height=600, plot_width=600, title="Products",
           toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
    plot.title.text_font_size = '20pt'
    
    plot.xaxis.major_label_text_font_size = "14pt" 
    plot.line(weeks, patients)
    plot.legend.label_text_font_size = '14pt'

    script, div = components(plot)
    
    #return render(request, 'starter.html', {'script': script, 'div': div})


    return render(request, 'starter.html' , {'script': script, 'div':div})
