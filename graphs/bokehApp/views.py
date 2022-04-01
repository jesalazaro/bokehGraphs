from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool


def starter(request):
    plot = figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size = 20, color = "blue")

    script, div = components(plot)


    return render(request, 'starter.html', {'script': script, 'div': div})
