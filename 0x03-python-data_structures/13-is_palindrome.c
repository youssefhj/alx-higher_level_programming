#include "lists.h"

/**
 * check - checker
 * @head: head of the list
 * @e: end of the list
 *
 * Return: 1 or 0
 */
int check(listint_t **head, listint_t *e)
{
	if (e == NULL)
		return (1);

	if (check(head, e->next) && e->n == (*head)->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if not a palindrome 1 otherwize
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	return (check(head, *head));
}
