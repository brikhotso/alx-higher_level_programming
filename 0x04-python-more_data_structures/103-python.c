#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_hexn(const char *str, int n);

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
 * print_hexn - Print hexadecimal representation of a string up to n characters
 * @str: The input string
 * @n: The number of characters to print
 */
void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
		printf("%02x ", (unsigned char) str[i]);

	printf("%02x", str[i]);
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Python object pointer
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *string = (PyBytesObject *) p;
	long int bytes, string_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(string))
	{
		string_size = PyBytes_Size(p);
		bytes = string_size + 1;

		if (bytes >= 10)
			calc_bytes = 10;

		printf("  size: %d\n", string_size);
		printf("  trying string: %s\n", string->ob_sval);
		printf("  first %d bytes: ", bytes);
		print_hexn(string->ob_sval, bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
