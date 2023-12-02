#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_infor - print basic info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *plist;
	Py_ssize_t list_size, i;
	PyObject *element;

	plist = (PyListObject *)p;
	list_size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", plist->allocated);

	for (i = 0; i < list_size; ++i)
	{
		element = PyList_GET_ITEM(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
