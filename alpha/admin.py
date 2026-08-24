
# Register your models here.
from django.contrib import admin

from alpha.models import Doctor, Patient, Appointment

# admin.site.register(Doctors)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','specialization','email','phone','consultation_fees')
    search_fields = ('specialization','consultation_fees')
    list_filter = ('name','specialization','email','phone','consultation_fees')

admin.site.register(Doctor, DoctorAdmin)

# Register Patient Model
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'dob', 'email', 'address', 'blood_group', 'created_at', 'updated_at')
    list_filter = ('blood_group', 'gender')
    search_fields = ('name',)
admin.site.register(Patient, PatientAdmin)


# Register Appointment Model
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'remarks', 'status', 'created_at', 'updated_at')

admin.site.register(Appointment, AppointmentAdmin)
