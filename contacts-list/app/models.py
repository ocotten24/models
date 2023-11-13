from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    is_favorite = models.BooleanField()

def create_contact(name, email, phone, is_favorite):
    newContact = Contact(name = name, email = email, phone = phone, is_favorite = is_favorite)
    newContact.save()
    return newContact

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(name):
    try:
        return Contact.objects.get(name = name)
    except:
        return None

def favorite_contacts():
    return Contact.objects.filter(is_favorite = True)

def update_contact_email(name, new_email):
    getContact = Contact.objects.get(name = name)
    getContact.email = new_email
    getContact.save()
    return getContact

def delete_contact(name):
    getContact = Contact.objects.get(name = name)
    getContact.delete()
    return getContact