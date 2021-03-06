from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import random
from models import Ticket
from datetime import datetime
from datetime import timedelta
from udj.headers import getTicketHeader
from udj.headers import getUserIdHeader
from udj.headers import getDjangoTicketHeader

def getUserForTicket(request):
  return Ticket.objects.get(
    ticket_hash=request.META[getDjangoTicketHeader()]).user

def ticketMatchesUser(request, provided_user_id):
  matchingTickets = Ticket.objects.filter(
    ticket_hash=request.META[getDjangoTicketHeader()], 
    user__id=provided_user_id)
  return len(matchingTickets) > 0
  

def isValidTicket(provided_hash):
  try:
    matchingTicket = Ticket.objects.get(ticket_hash=provided_hash)
  except DoesNotExist:
    return False
  if(datetime.now() - matchingTicket.time_issued).days < 1:
    return True
  else:
    return False

def validAuthRequest(request):
  if not request.method == "POST":
    return False
  elif not request.POST.__contains__("username") \
    or not request.POST.__contains__("password"):
    return False
  return True
  

def generateRandomHash():
  rand_hash = random.getrandbits(128)
  toReturn = "%032x" % rand_hash
  return toReturn

def getUniqueRandHash():
  rand_hash = generateRandomHash()
  while Ticket.objects.filter(ticket_hash=rand_hash):
    rand_hash = generateRandomHash()
  return rand_hash


def getTicketForUser(userRequestingTicket):
  currentTickets = Ticket.objects.filter(user=userRequestingTicket)
  if currentTickets:
    for ticket in currentTickets:
      ticket.delete()
  toReturn = Ticket(user=userRequestingTicket, ticket_hash=getUniqueRandHash())
  toReturn.save()
  return toReturn 


@csrf_exempt
def authenticate(request):
  if not validAuthRequest(request):
    return HttpResponseBadRequest()

  userToAuth = get_object_or_404( \
    User, username__exact=request.POST['username'])
  if userToAuth.check_password(request.POST['password']):
    ticket = getTicketForUser(userToAuth)
    response = HttpResponse()
    response[getTicketHeader()] = ticket.ticket_hash
    response[getUserIdHeader()] = userToAuth.id
    return response
  else:
    return HttpResponseForbidden()
