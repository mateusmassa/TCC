#include<stdio.h>
#include<unistd.h>
#include<signal.h>
 
void sig_handler(int signum){
 
  printf("Função de handler interna\n");
 
  alarm(5);  // Schedule a new alarm after 5 seconds
}
 
int main(){
 
  signal(SIGALRM,sig_handler); // Register signal handler
 
  alarm(5);  // Schedule the first alarm after 5 seconds
 
  for(int i=1;;i++){
 
    printf("%d : Função principal interna \n",i);
    pause(); // waiting until signal is handled
}
 
return 0;
}
