from django.shortcuts import render
from django.views.generic.base import TemplateView
from students.models import Payment,Students
from groups.models import Group
from teachers.models import Teacher
from django.views import View
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .forms import  UnpaidPaymentsFilterForm

class Home(TemplateView):
    template_name = 'index.html'


class AllFinance(View):
    template_name = 'moliya/moliya.html'
    
    def get_context_data(self,**kwargs):
        kwargs = {
            'groups':Group.objects.all(),
            'payments': Payment.objects.annotate(month=TruncMonth('date_added')).values('month').annotate(sum=Sum('amount')),
            'teachers':Teacher.objects.all(),
            'all_payments':Payment.objects.all(),
        }
        return kwargs

    def get(self, request,*args,**kwargs):
        context = self.get_context_data()
        if 'filter' in request.GET:
            by_date = request.GET.get('by_date')
            by_name = request.GET.get('by_name')
            by_phone = request.GET.get('by_phone')
            by_teacher = request.GET.get('by_teacher')
            if by_date:
                context['all_payments'] = Payment.objects.filter(date_added=by_date)
            elif by_name:
                context['all_payments'] = Payment.objects.filter(student__name__icontains=by_name)
                print(context)
            elif by_phone:
                context['all_payments'] = Payment.objects.filter(student__phone__icontains=by_phone)
            elif by_teacher:
                context['all_payments'] = Payment.objects.filter(course__teacher__name__icontains=by_teacher)
            else:
                context['all_payments'] = Payment.objects.all()
                return render(request, self.template_name, context)
        return render(request,self.template_name,context)


    def post(self,request,*args,**kwargs):
        context = {}
        return render(request,self.template_name, self.get_context_data(**context))


class Salary(View):
    template_name = 'moliya/moliya_4.html'

    def get_context_data(self,*args,**kwargs):
        context = {
            'teachers':Teacher.objects.all(),
            'salary':''
        }
        return context
    
    def get(self,request,*args,**kwargs):
        context = self.get_context_data()
        if 'calculate' in request.GET:
            started_date = request.GET.get('from')
            to = request.GET.get('to')
            salary = Payment.objects.filter(course__teacher__id=request.GET.get('teacher'),date_added=started_date,).aggregate(total_salary=Sum('course__price'))
            context['salary'] = salary
            return render(request,self.template_name,context)
        return render(request,self.template_name,context)
    


    def post(self,request,*args,**kwargs):
        context = self.get_context_data()
        return render(request,self.template_name,context)
    


class Debts(TemplateView):
    template_name = 'moliya/moliya_5.html'


# class Debts(View):
#     template_name = 'moliya/moliya_5.html'

#     def get_context_data(self,*args,**kwargs):
#         return kwargs

#     def get(self,request,*args,**kwargs):
#         context = self.get_context_data()
#         month = request.GET.get('month')
#         student = request.GET.get('student')
#         context['debts'] = Payment.objects.filter(student__name__icontains=student).filter()
#         return render(request,self.template_name,context)
    

#     def post(self,request,*args,**kwargs):
#         context = {}
#         return render(request,self.template_name,context)
