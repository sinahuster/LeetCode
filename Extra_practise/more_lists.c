// Practise for creating linked lists and functions 

#include <stdio.h>
#include <stdlib.h>

typedef struct node 
{
    int value;
    struct node *next;
}node;

void list_print(node *list);
void list_free(node **list);
void list_prepend(node **list, int val);
void list_append(node **list, int val);
node* list_reverse(node *list);
int list_middle(node **list, int val, int position);

int main(void)
{
    // create an empty list to test funtions on
    node *empty = NULL;
    list_print(empty);
    list_reverse(empty);
    list_append(&empty, 1);
    list_print(empty);
    list_free(&empty);
    node *emp = NULL;
    list_print(emp);
    list_prepend(&emp, 1);
    list_print(emp);
    list_middle(&emp, 5, 3);
    list_free(&emp);

    // create a populated list to test the functions on
    int array[] = {1, 2, 3, 4};
    node *pop = NULL;
    for (int i = 0; i < (sizeof(array)/sizeof(array[0])); i++)
    {
        list_append(&pop, array[i]);
    }
    list_print(pop);
    list_prepend(&pop, 0);
    list_print(pop);
    list_append(&pop, 5);
    list_print(pop);
    list_middle(&pop, 10, 3);
    list_print(pop);
    node *reverse = list_reverse(pop);
    list_print(reverse);
    list_free(&reverse);
    list_free(&pop);

    return 0;
}

void list_print(node *list)
{
    while (list != NULL)
    {
        printf("%i, ", list->value);
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

    // just for safety 
    *list = NULL;

    return;
}

void list_append(node **list, int val)
{
    node *new = malloc(sizeof(node));
    new->value = val;
    new->next = NULL;

    if (*list == NULL)
    {
        *list = new;
        return;
    }

    node *tail = *list;
    while(tail->next != NULL)
    {
        tail = tail->next;
    }

    tail->next = new;

    return;
}

void list_prepend(node **list, int val)
{
    node *new = malloc(sizeof(node));
    new->value = val;
    new->next = *list;
    *list = new;

    return;
}

node* list_reverse(node *list)
{
    node *reverse = NULL;

    while (list != NULL)
    {
        list_prepend(&reverse, list->value);
        list = list->next;
    }

    return reverse;
}

int list_middle(node **list, int val, int position)
{
    if (*list == NULL)
    {
        printf("Unable to add in the middle as this position doesn't exsist.\n");
        return -1;
    }

    node *new = malloc(sizeof(node));
    new->value = val;
    new->next = NULL;

    node *tail = *list;

    for (int i = 1; i < position - 1; i++)
    {
        if(tail->next == NULL)
        {
            printf("Unable to add in the middle as this position doesn't exsist.\n");
            return -1;
        }
        tail = tail->next;
    }

    new->next = tail->next;
    tail->next = new;

    return 0;
}




