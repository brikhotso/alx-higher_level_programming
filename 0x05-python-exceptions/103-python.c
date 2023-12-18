#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print information about a Python list object
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t i;
    char *str;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str ? str : "(no allocation)");

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i)
    {
        printf("%02hhx", str[i]);
        if (i + 1 < size && i + 1 < 10)
        {
            printf(" ");
        }
    }
    printf("\n");
}

/**
 * print_python_float - Print information about a Python float object
 * @p: Pointer to the Python float object
 */
void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;

    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
