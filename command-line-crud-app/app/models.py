from django.db import models

# Create your models here.

class ToDoList(models.Model):
    is_starred = models.BooleanField()
    todoDescription = models.CharField(max_length=250)
    todoTopic = models.CharField(max_length=250)

def createTodo(is_starred, todoDescription, todoTopic):
    todoVariable = ToDoList(
    is_starred = is_starred,
    todoDescription = todoDescription,
    todoTopic = todoTopic
    )
    todoVariable.save()
    return todoVariable

def showAll():
    return ToDoList.objects.all()

def showAllStarred():
    return ToDoList.objects.filter(is_starred = True)

def findByTopic(todoTopic):
    try:
        return ToDoList.objects.get(todoTopic = todoTopic)
    except:
        return None

def updateToDo(id, newTopic, newDescription):
    specificItem = ToDoList.objects.get(id = id) 
    specificItem.todoDescription = newDescription
    specificItem.todoTopic = newTopic
    specificItem.save()
    return specificItem

def deleteTodo(id):
    specificItem = ToDoList.objects.get(id = id) 
    specificItem.delete()
    return specificItem
