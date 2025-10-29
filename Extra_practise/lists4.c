#include <stdio.h>
#include <stdlib.h>

typedef struct node 
{
    int val;
    struct node *next;
}node;

void list_print(node *list);
void list_free(node **list);
void list_prepend(node **list, int value);
void list_append(node **list, int value);
void list_middle(node **list, int value, int position);
node *list_reverse(node *list);

int main(void)
{
    node *empty = NULL;
    list_append(&empty, 0);
    // list_prepend(&empty, 0);
    list_print(empty);
    list_middle(&empty, 1, 3);
    list_reverse(empty);
    list_print(empty);
    list_free(&empty);

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
    list_append(&list, 5);
    list_print(list);
    list_middle(&list, 4, 5);
    list_print(list);
    node *reversed = list_reverse(list);
    list_print(reversed);
    list_free(&list);

    return 0;
}

void list_print(node *list)
{
    while (list != NULL)
    {
        printf("%i", list->val);
        list = list->next;
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

void list_append(node **list, int value)
{
    node *new = malloc(sizeof(node));
    new->next = NULL;
    new->val = value;

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

    return;
}

void list_prepend(node **list, int value)
{
    node *new = malloc(sizeof(node));
    new->val = value;

    new->next = *list;
    *list = new;

    return;
}

void list_middle(node **list, int value, int position)
{
    if (*list == NULL)
    {
        printf("The position does not exsit.\n");
        return;
    }

    node *new = malloc(sizeof(node));
    new->next = NULL;
    new->val = value;

    node *ptr = *list;

    for (int i = 1; i < position - 1; i++)
    {
        if (ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        else 
        {
            printf("The position does not exsit.\n");
            return;
        }
    }

    new->next = ptr->next;
    ptr->next = new;
}

node *list_reverse(node *list)
{
    if (list == NULL)
    {
        return list;
    }

    node *reversed = NULL;

    while (list != NULL)
    {
        list_prepend(&reversed, list->val);
        list = list->next;
    }

    return reversed;
}