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
	while (pre && pre->next)
	{
		curr = curr->next;
		pre = pre->next->next;
		if (curr == pre)
			return (1);

	}

	return (0);
}
