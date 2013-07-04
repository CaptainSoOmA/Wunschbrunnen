# Create your views here.
from Zettel.models import Zettel, BibInfo
from Zettel.form import ZettelForm , BibInfoZettel 

from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import RequestContext


def index(request):
	# maybe better umbiegen
	return all_zettel(request)

def new_zettel(request):
	if request.method == 'POST': 

		# falls Daten uebermittelt wurden
		form_zettel = ZettelForm(request.POST, instance=Zettel())
		form_bib = BibInfoZettel(request.POST, instance=BibInfo()) 

		
		if form_zettel.is_valid():
			tmpZettel = form_zettel.save(commit=False)
			tmpZettel.pub_date = datetime.now()

			if form_bib.is_valid():
				tmpZettel.save()
				tmpBib = form_bib.save()
				tmpZettel.bib.add(tmpBib)

			tmpZettel.save()

		return HttpResponseRedirect('/') # Redirect after POST
	else:
		form_zettel = ZettelForm() # An unbound form
		form_bib = BibInfoZettel()


	return render(request, 'new.html', {
		'form_zettel'	: form_zettel,
		'form_bib'		: form_bib,
	})

def insert_zettel(request):

	html = []
	
	for k in request.POST:
		html.append('<tr><td>' + k+ '</td><td>'+ request.POST[k]+'</td></tr>' )
	return HttpResponse('<table>%s</table>' % '\n'.join(html))


def zettel(request,zettel_id):
	z = get_object_or_404(Zettel, pk=zettel_id)
	return render_to_response('zettel.html',{'zettel':z})

def all_zettel(request):
	latest_zettel_list = Zettel.objects.all().order_by('pub_date')[:5]
	return render_to_response('all.html',{'latest_zettel_list':latest_zettel_list})