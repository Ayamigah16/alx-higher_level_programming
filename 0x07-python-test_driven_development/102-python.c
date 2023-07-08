#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: The Python string object
 *
 * This function prints information about the given Python string object,
 * including its type, length, and value.
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    const char *value;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AsUTF8(p);

    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    printf("  length: %ld\n", length);
    printf("  value: %s\n", value);
}
