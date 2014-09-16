from django.shortcuts import render
from resistance.forms import ColorCodeForm
from django.http import StreamingHttpResponse
import math

# Create your views here.

def calculate(request):
	p = ''
	res = 0
	tolerance = 0
	if request.method == 'POST':
		form = ColorCodeForm(request.POST)
		band1 = int(request.POST.get('band1', ''))
		band2 = int(request.POST.get('band2', ''))
		band3 = int(request.POST.get('band3', ''))
		tolerance = int(request.POST.get('tolerance', ''))
		if form.is_valid():

			res = float(( band1 * 10 + band2 ) * pow(10,band3))
			if res in range(0,1000):
				pass
			if res in range(1000,1000000):
				res = res/1000
				p = 'Kilo'
							
			return render(request, 'resistance.html', {'form':form, 'res':res,'p':p, 'tolerance':tolerance})
	else:
		form = ColorCodeForm()

	return render(request, 'resistance.html', {'form':form, 'res':res, 'tolerance':tolerance })
