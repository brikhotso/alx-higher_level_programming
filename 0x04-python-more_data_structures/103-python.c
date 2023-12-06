#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print python list information
 * @p: Python object pointer
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Python object pointer
 */
void print_python_bytes(PyObject *p)
{
	long int size = 0, i = 0;
	char *string_data;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}

	string_data = PyUnicode_AsUTF8(PyObject_Str(p));

	if (string_data != NULL)
	{
		size = strlen(string_data);
	}

	printf("[.] bytes object info\n");
	printf("  [.] Size: %ld\n", size);
	printf("  [.] trying string: %s\n", string_data);

	printf("  [.] first 10 bytes:");
	for (i = 0; i < size; ++i)
	{
		if (i < 10)
			printf(" %02x", (unsigned char)string_data[i]);
	}
	printf("\n");
}
