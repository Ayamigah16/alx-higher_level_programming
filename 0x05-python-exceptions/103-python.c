#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

size = PyList_Size(p);
for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", str);
printf("  first %zd bytes:", size + 1 < 10 ? size + 1 : 10);
for (i = 0; i < size + 1 && i < 10; i++)
{printf(" %02x", str[i] & 0xff); }
printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
PyObject *repr;

printf("[.] float object info\n");
if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

repr = PyObject_Repr(p);
printf("  value: %s\n", PyUnicode_AsUTF8(repr));
Py_DECREF(repr);
}
