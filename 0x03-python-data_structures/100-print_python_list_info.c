#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: Pointer to a PyObject representing a Python list
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

size = PyList_Size(p);
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
