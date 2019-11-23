//#include "GameLogic.h"

#include "GameLogic.h"

int main(int argc, char *argv[])
{
	if (argc < 5)
	{
		cout << "Invalid Parameters" << endl;
		return 0;
	}
	//mode="m"->manual/"t"->tournament
	int col = atoi(argv[1]);
	int row = atoi(argv[2]);
	int p = atoi(argv[3]);
	string mode = argv[4];
	int order = 0;
<<<<<<< HEAD
    if (mode == "m" or mode == "manual")
=======
    if (mode == "m" || mode == "manual"|| mode == "s"|| mode == "self")
>>>>>>> 910384cfb286446520800052955f01d9021cbbac
    {
        order = atoi(argv[5]);
    }
	GameLogic main(col,row,p, mode, order);//col,row,p,g,mode,debug
	main.Run();

	return 0;
}
