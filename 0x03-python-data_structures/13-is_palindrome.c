#include "lists.h"

/**
 * reverse_list - reverse a linked list
 * @head: first item in a linked list
 * Return: reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - check if list reads the same backwards and forward
 * @head: pointer to first item in a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *forward = *head;
	listint_t *back = reverse_list(slow);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	while (back != NULL)
	{
		if (forward->n != back->)
			return (0);

		forward = forward->next;
		back = back->next;
	}

	return (1);
}
