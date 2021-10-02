#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void * configuration(void)
{
	FILE* config;
	config = fopen("config.txt", "r");
	if (config == NULL)
	{
		static char convert_ch[14] = { ' ', '.', '`', ':', '~', '*', '=', '&', '%', '#' };
		FILE* write_config = fopen("config.txt", "w");
		for (int x = 0; x < 10; x++)
			fprintf(write_config, "%d %c\n", x, convert_ch[x]);
		fclose(write_config);
	}
}


int * get_launch_parameters(int argc, char* argv[], int* get_param)
{
	const char valid_parameter[4][4] = { "-l", "-w", "-t" };
	int long_param;
	int width_param;
	int element_limit;
	int x, y;
	for (x = 1, y =0; x < argc; x = x+2 )
	{
		if (strcmp(argv[x], valid_parameter[y]) == 0)
		{
			if (y == 0)
				long_param = atoi(argv[x + 1]);
			if (y == 1)
				width_param = atoi(argv[x + 1]);
			if (y == 2)
				element_limit = atoi(argv[x + 1]);
			y++;
			x = 1;
		}
	}
	if (&long_param == NULL || long_param == 0)
		long_param = 30;
	if (&width_param == NULL || width_param == 0)
		width_param = 30;
	if (&element_limit == NULL || element_limit == 0)
		element_limit = 10;
	get_param[0] = long_param;
	get_param[1] = width_param;
	get_param[2] = element_limit;
	return get_param;
}

int main(int argc, char* argv[])
{
	if (argc > 7)
	{
		printf("please check parameter!\n");
		return 3;
	}
	int long_limit, width, type_limit;
	int* launch_param;
	int get_param[3];
	launch_param = get_launch_parameters(argc, argv, get_param);
	long_limit = launch_param[0];
	width = launch_param[1];
	type_limit = launch_param[2];
	int romdom_num;
	FILE* export;
	export = fopen("export.txt", "w");
	if (export == NULL)
	{
		printf("export is failed!\n");
		exit(4);
	}
	int x = 1;
	int y = 1;
	while (y <= width)                                             
	{
		romdom_num = rand() % type_limit;
		printf("%d", romdom_num);
		fprintf(export, "%d", romdom_num);
		x++;
		if (x >= long_limit)
		{
			if (x == long_limit)
				putc(' ', export);
			putc('\n', export);
			putchar('\n');
			y++;
			x = 1;
		}
		else
		{
			putc(' ', export);
			putchar(' ');
			x++;
		}
	}               
	if (fclose(export) != 0)           	/*文件关闭及相关提示*/
	{
		printf("\nError in closing output-file \n");
		exit(2);
	}
	printf("\nclose file comlete!\n");
	exit(0);
}
