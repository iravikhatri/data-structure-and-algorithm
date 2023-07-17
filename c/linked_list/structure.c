// basic implementation of list

#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

struct Node* head = NULL;;

struct Node* newNode();
void printList();
void insertAtStart(int);
void insertAtEnd(int);

void main(){
    int input = 1, number;

    while (input) {
        printf("\nPress 1 for print the list \nPress 2 for insert an element in list \nPress 0 for quit \n");
        scanf("%d", &input);

        if(input == 1){
            printList();
        }
        else if(input == 2){
            printf("Enter a number : ");
            scanf("%d", &number);
            insertAtEnd(number);
        }
    }

}

struct Node* newNode(){
    return (struct Node*)malloc(sizeof(struct Node));
}

void printList(){
    struct Node* temp = head;
    while(temp != NULL){
        printf("%d ",temp->data);
        temp = temp->next;
    }
}

void insertAtStart(int value){
    struct Node* temp = newNode();
    temp->data = value;
    temp->next = head;
    head = temp;
}

void insertAtEnd(int value) {
    struct Node* temp = newNode();
    temp->data = value;
    temp->next = NULL;

    struct Node* temp_head = head;

    if(head == NULL){
        head = temp;
    }
    else{
        while(temp_head->next != NULL) {
            temp_head = temp_head->next;
        }
        temp_head->next = temp;
    }
}
