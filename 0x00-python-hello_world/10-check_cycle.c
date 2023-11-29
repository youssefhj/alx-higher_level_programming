#include "lists.h"

/**
 * check_cycle - check if list has a cycle
 * @list: list
 *
 * Return: 0 if there is no cycle 1 otherwize
 */
int check_cycle(listint_t *list)
{
	listint_t *pre, *curr;

	pre = curr = list;
	while (curr)
	{
		curr = curr->next;
		if (curr->next == pre)
			return (1);

		pre = curr;
	}

	return (0);
}
