// Creating a various functions for a linked list 

#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int value;
    struct node *next;

} node;

void list_print(node *list);
void list_prepend(node** list, int val);
void list_append(node** list, int val);
node* list_reverse(node* list);
void list_free(node** list);

int main(void)
{

    int arr[] = {1, 2, 3, 4, 5};

    // Populating list 
    node *list = NULL;
    node *one = NULL;
    node *two = NULL;
    node *three = NULL;

    list_print(one);
    list_prepend(&one, 1);
    list_print(one);
    list_append(&two, 2);
    list_print(two);
    list_reverse(three);
    list_print(three);
    list_free(&three);
    list_print(three);
    
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
    {
        node *cur_node = malloc(sizeof(node));

        cur_node->next = NULL;
        cur_node->value = arr[i];

        cur_node->next = list;
        list = cur_node;

    }

    list_print(list);
    list_prepend(&list, 6);
    list_print(list);
    list_append(&list, 0);
    list_print(list);
    list_print(list_reverse(list));
    list_free(&list);

    return 0;
}

void list_print(node *list) {

    // Printing list 
    node *temp = list;
    while (temp != NULL)
    {
        printf("%i, ", temp->value);
        temp = temp->next;
    }
    printf("\n");

    return;
}

void list_prepend(node** list, int val) {

    node *cur_node = malloc(sizeof(node));

    cur_node->next = NULL;
    cur_node->value = val;

    cur_node->next = *list;
    *list = cur_node;

    return;
}

void list_append(node** list, int val) {

    node *cur_node = *list;
    node *new = malloc(sizeof(node));

    new->next = NULL;
    new->value = val;

    if ((*list) == NULL)
    {
        (*list) = new;
        return;
    }

    while (cur_node->next != NULL)
    {
        cur_node = cur_node->next;
    }

    cur_node->next = new;

    return;
}

node* list_reverse(node* list) {

    node *reversed = NULL;

    while(list != NULL)
    {
        list_prepend(&reversed, list->value);
        list = list->next;
    }
    
    return reversed;
}

void list_free(node** list){

    while (*list != NULL)
    {
        node *ptr = *list;
        *list = (*list)->next;
        free(ptr);
    }

    *list = NULL;

    return;
}