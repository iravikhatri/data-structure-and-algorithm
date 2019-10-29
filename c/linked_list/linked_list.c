// basic implementation of list

#include <stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

struct Node* head;

void printList();
void insert(int head);

void main(){

    head = NULL;
    int input = 1, number;

    while (input) {
        printf("\nPress 1 for print the list \nPress 2 for insert an element in list \nPress 0 for quit \n");
        scanf("%d", &input);

        if(input == 1){
            printList();
        }
        else if(input == 2){
            printf("Enter a number\n");
            scanf("%d", &number);
            insert(number);
        }
    }

}

void printList(){
    struct Node* temp = head;
    while(temp != NULL){
        printf("%d ",(*temp).data);
        temp = (*temp).next;
    }
    printf("\n");
}

void insert(int value){
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    (*temp).data = value;
    (*temp).next = head;
    head = temp;
    printList();
}
