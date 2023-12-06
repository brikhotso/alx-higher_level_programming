#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print python list information
 * @p: Python object pointer
 */
void print_python_list(PyObject *p)
{
	long int size = 0, i = 0;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	while (1)
	{
		item = PyList_GetItem(p, size);
		if (item == NULL)
			break;
		size++;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		if (item != NULL)
		{
			printf("[*] Element %ld: %s\n", i,
			       item->ob_type->tp_name);
		}
		else
		{
			printf("[*] Element %ld: Unknown\n", i);
		}
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
