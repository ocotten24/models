from django.test import TestCase
from app import models

# Create your tests here.

class TestList(TestCase):
    def test_can_create_todo(self):
        todo = models.createTodo(
            True,
            "clean house",
            "clean"
        ) 
        self.assertEqual(todo.is_starred, True)
        self.assertEqual(todo.todoDescription, 'clean house')
        self.assertEqual(todo.todoTopic, 'clean')

    
    def test_see_all(self):
        todoOne = models.createTodo(
            True,
            "clean house",
            "clean"
        )

        todoTwo = models.createTodo(
            False,
            "feed cat",
            "feed"
        )

        todoThree = models.createTodo(
            True,
            "refuel car",
            "refuel"
        )

        allTodos = models.showAll()
        self.assertEqual(len(allTodos), 3)



    def test_see_all_starred(self):
        todoOne = models.createTodo(
            True,
            "clean house",
            "clean"
        )

        todoTwo = models.createTodo(
            False,
            "feed cat",
            "feed"
        )

        todoThree = models.createTodo(
            True,
            "refuel car",
            "refuel"
        )

        allTodos = models.showAllStarred()
        self.assertEqual(len(allTodos), 2)

    
    def test_see_all_starred(self):
        todoOne = models.createTodo(
            True,
            "clean house",
            "clean"
        )

        todoTwo = models.createTodo(
            False,
            "feed cat",
            "feed"
        )

        todoThree = models.createTodo(
            True,
            "refuel car",
            "refuel"
        )

        allTodos = models.showAllStarred()
        self.assertEqual(len(allTodos), 2)


    
    def test_see_specific_todo(self):
        todoOne = models.createTodo(
            True,
            "clean house",
            "clean"
        )

        todoTwo = models.createTodo(
            False,
            "feed cat",
            "feed"
        )

        todoThree = models.createTodo(
            True,
            "refuel car",
            "refuel"
        )

        allTodos = models.findByTopic("refuel")
        self.assertEqual(allTodos.todoDescription, "refuel car")

        allTodosFalse = models.findByTopic("asaksdmdkasdmkasmdksad")
        self.assertIsNone(allTodosFalse)

    
    def test_update_list(self):
        todo = models.createTodo(
            True,
            "clean house",
            "clean"
        ) 

        updatedTodo = models.updateToDo(todo.id, 'newTopic', 'newDescription')

        self.assertEqual(updatedTodo.todoTopic, 'newTopic')
        self.assertEqual(updatedTodo.todoDescription, 'newDescription')


    def test_delete(self):
        todoOne = models.createTodo(
            True,
            "clean house",
            "clean"
        )

        todoTwo = models.createTodo(
            False,
            "feed cat",
            "feed"
        )

        todoThree = models.createTodo(
            True,
            "refuel car",
            "refuel"
        )

        models.deleteTodo(2)
        self.assertEqual(len(models.showAll()), 2)
        