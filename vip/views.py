from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse, JsonResponse

from TicketLink.models import Member, Agreement, Agree, Vip, Booking, Reservations
from TicketLink.models import Notice, NoticeCate, Guide
from TicketLink.models import InquiryType, InquiryStep, Inquiry, Answer
from TicketLink.models import Event, EventCate, EventEntry

from TicketLink.models import Bank, Event, EventEntry, Perform, Write, BkCancel
# from TicketLink.models import Document, DocCate, CancelTicket, Priorty, RefundAccount

from datetime import date, datetime, timedelta
from django.core.paginator import Paginator
from dateutil.relativedelta import relativedelta

# Create your views here.


def index(request:HttpRequest):
    try:
        member = Member.objects.get(member_no = request.session.get('login'))
    except Exception as e:
        print(e)
        member = None
    list = Perform.objects.filter(perform_no__lte = 4)
    vip = Vip.objects.get(vip_no = 4)
    context = {
        "member" : member,
        "list" : list,
        "vip" : vip,
    }
    return render(request, 'vip/index.html', context)