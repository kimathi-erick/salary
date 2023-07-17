from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import workerform,attendanceform,updateattendance,registrationform
from django.core.exceptions import ValidationError
import xlwt
from django.contrib.auth.decorators import login_required

# Create your views here.
def registrationview(request):
    if request.method == 'POST':
        form=registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=registrationform()   
    context={
        'form':form
    }         
    return render(request,'register.html',context)
@login_required    
def workerslist(request):
    workers=worker.objects.all()
    p= worker.total_pending_payments()
    if request.method == 'POST':
        form=workerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workerslist')
    else:
        form=workerform()        
    context={
        'workers':workers,
        'form':form,
        'p':p
    }
    return render(request,'workers.html',context)
@login_required 
def deleteworker(request,pk):
    aworker=worker.objects.get(id=pk)
    aworker.delete()
    return redirect('workerslist') 
@login_required     
def deleteattendance(request,pk):
    aworker=attendance.objects.get(id=pk)
    aworker.delete()
    return redirect('attendancelist')        
@login_required 
def attendancelist(request):
    attendances = attendance.objects.all().order_by('date')
    if request.method == 'POST':
        form = attendanceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendancelist')
    else:
        form = attendanceform() 
    context={
        'form': form,
        'attendances': attendances
    }
    return render(request, 'attendance.html', context)
@login_required 
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            workers=worker.objects.filter(First_Name__icontains=query)
            context={
                'workers': workers,
            }
        else:
            print('Name not found')
    return render(request,'search.html',context)  
@login_required 
def updateattendanceview(request,pk):
    attendant=attendance.objects.get(id=pk)
    if request.method == 'POST':
        form = attendanceform(request.POST,instance=attendant)
        if form.is_valid():
            form.save()
            return redirect('attendancelist')
    else:
        form=attendanceform(instance=attendant)  
    context={
        'form':form
    }  
    return render(request,'updateform.html',context)  
@login_required      
def salaryview(request):
    attendances = worker.objects.all()
    p= worker.total_pending_payments()

    # Create a new workbook and add a sheet named 'Attendance'
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Attendance')

    # Write the headers to the Excel sheet
    ws.write(0, 0, 'First_Name')
    ws.write(0, 1, 'Id_Number')
    ws.write(0, 2, 'Amount_Payable')
    ws.write(0, 3, 'Total')

    # Write the attendance data to the Excel sheet
    for i, attendance in enumerate(attendances, start=1):
        ws.write(i, 0, attendance.First_Name)
        ws.write(i, 1, attendance.Id_Number)
        ws.write(i, 2, attendance.pending_payments())
    # Save the Excel file to a file named 'attendance.xls'
    wb.save('attendance.xls')

    # Render the template with the attendance data
    context = {
        'attendances': attendances,
        'p':p
    }
    return render(request, 'salary.html', context)



            
