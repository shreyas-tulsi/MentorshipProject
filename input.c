#include <stdio.h>
#include <stdlib.h>


int main(int argc, char*argv[])
{
  fprintf(stdout,"%s",argv[1]);
  FILE * input1 = fopen("input1.txt","w");
  char * mode = argv[1];
  fwrite(mode,1,10,input1);
  system("python3 main.py");
}