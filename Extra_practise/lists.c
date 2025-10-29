#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int value;
    struct node *next;
}node;

void list_print(node *list);
void list_free(node **list);
node *list_prepend(node **list, int val);
node *list_append(node **list, int val);
node *list_middle(node **list, int val, int pos);
node *list_reverse(node *list);

int main(void)
{
/*
    node *empty = NULL;
    list_prepend(&empty, 0);
    list_print(empty);
    list_append(&empty, 0);
    list_print(empty);
    list_free(&empty);
*/
    int array[] = {1, 2, 3};

    node *list = NULL;
    
    int size = sizeof(array) / sizeof(array[0]);

    for (int i = 0; i < size; i++)
    {
        list_append(&list, array[i]);
    }

    list_print(list);
    list_prepend(&list, 0); 
    list_print(list);
    list_middle(&list, 4, 3);
    list_middle(&list, 3, -3);
    list_middle(&list, 3, 10);
    list_print(list);
    node *reverse = list_reverse(list);
    list_print(reverse);
    list_free(&list);
    list_free(&reverse);
}

void list_print(node *list)
{
    node *ptr = list;
    while (ptr != NULL)
    {
        printf("%i ", ptr->value);
        ptr = ptr->next;
    }
    printf("\n");

    return;
}

void list_free(node **list)
{
    while (*list != NULL)
    {
        node *ptr = *list;
        *list = (*list)->next;
        free(ptr);
    }

    return;
}

node *list_prepend(node **list, int val)
{
    node *new = malloc(sizeof(node));
    new->value = val;
    new->next = NULL;

    if (*list == NULL)
    {
        *list = new;
    }
    else 
    {
        new->next = *list;
        *list = new;
    }

    return *list;
}

node *list_append(node **list, int val)
{
    node *new = malloc(sizeof(node));
    new->value = val;
    new->next = NULL;
    
    if (*list == NULL)
    {
        *list = new;
    }
    else 
    {
        node *ptr = *list;
        while (ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        ptr->next = new;
    }

    return *list;
}

node *list_middle(node **list, int val, int pos)
{
    node *new = malloc(sizeof(node));
    new->next = NULL;
    new->value = val;

    if (pos < 0)
    {
        printf("This position is not valid\n");
        return *list;
    }

    node *ptr = *list;

    for (int i = 0; i < pos - 1; i++)
    {
        if (ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        else 
        {
            printf("This position is not valid\n");
            return *list;
        }
    }

    new->next = ptr->next;
    ptr->next = new;

    return *list;
}

node *list_reverse(node *list)
{
    if (list == NULL)
    {
        return list;
    }
    
    node *reverse = NULL;

    while (list != NULL)
    {
        list_prepend(&reverse, list->value);
        list = list->next;
    }
    return reverse;
}