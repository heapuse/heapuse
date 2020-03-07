#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>


void *My_Func(void *idp) 
{
	long my_id = (long)idp;
  	printf("Starting watch_count(): thread %ld\n", my_id);
	printf("Hi! Welcome\n");
//	pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
  int i, rc;
  pthread_t threads[6];
  pthread_create(&threads[0],NULL, My_Func, (void *)2);
  pthread_create(&threads[1], NULL, My_Func, (void *)3);
  pthread_create(&threads[2], NULL, My_Func, (void *)4);
  pthread_create(&threads[3], NULL, My_Func, (void *)5);
  pthread_create(&threads[4], NULL, My_Func, (void *)0);
  pthread_create(&threads[5], NULL, My_Func, (void *)1);

  for (i = 0; i < 6; i++) {
    pthread_join(threads[i], NULL);
  }
  printf ("Main(): Waited on %d  threads. Done.\n", 6);
 // pthread_exit (NULL);

}


