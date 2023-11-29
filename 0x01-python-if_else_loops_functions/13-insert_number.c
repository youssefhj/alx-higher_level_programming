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
	listint_t *p1 = *head;
	listint_t *node;

	node = (listint_t *)malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;
	
	if (p1 == NULL || node->n < p1->n)
	{
		node->next = p1;
		return (*head = node);
	}


	while (p1)
	{
		if (p1->next == NULL || node->n < p1->next->n)
		{
			node->next = p1->next;
			p1->next = node;
			return (node);
		}
		p1 = p1->next;
	}
	
	return (NULL);
}
