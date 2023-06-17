#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the PyObject representing a Python list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyObject_Length(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyVarObject *)p)->ob_size);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((PyObject *)item)->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the PyObject representing a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %ld bytes:", (size < 10) ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", string[i] & 0xff);

	printf("\n");
}
