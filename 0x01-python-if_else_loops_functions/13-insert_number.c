#include "lists.h"

/**
 * insert_node - insert node
 * @head: head of the list
 * @number: number to add
 *
 * Return: address of the node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p1, *p2;
	listint_t *node;

	node = (listint_t *)malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	p1 = *head;
	p2 = *head->next;

	while (p2)
	{
		if (number > p1->n && number < p2->n)
		{
			p1->next = node;
			node->next = p2;
			return (node);
		}
		p1 = p2;
		p2 = p2->next;
	}

	p1->next = node;
	return (node);
}
